#!/usr/bin/env python3
"""Fetch AI HOT public data into versioned, frontend-safe snapshots.

The browser never calls AI HOT directly. This script is intended to run from a
scheduled job or CI workflow and only rewrites outputs when the upstream
fingerprint changes.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SNAPSHOT_PATH = DATA_DIR / "aihot.json"
ARCHIVE_PATH = DATA_DIR / "aihot_archive.json"
JS_PATH = ROOT / "aihot.js"
INDEX_PATH = ROOT / "index.html"

API_ROOT = "https://aihot.virxact.com/api/public"
DEFAULT_UA = "sequentry-atlas/1.0 (+https://sequentry.com)"


class FetchError(RuntimeError):
    """Raised when an upstream response cannot be safely consumed."""


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp")
    temp.write_text(text, encoding="utf-8")
    temp.replace(path)


def request_json(
    path: str,
    *,
    params: dict[str, Any] | None,
    user_agent: str,
    timeout: int,
    retries: int = 3,
) -> tuple[dict[str, Any], dict[str, str]]:
    query = f"?{urlencode(params)}" if params else ""
    url = f"{API_ROOT}{path}{query}"
    headers = {
        "Accept": "application/json",
        "User-Agent": user_agent,
    }

    for attempt in range(retries):
        request = Request(url, headers=headers)
        try:
            with urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
                data = json.loads(raw)
                if not isinstance(data, dict):
                    raise FetchError(f"Unexpected response shape from {path}")
                response_headers = {key.lower(): value for key, value in response.headers.items()}
                return data, response_headers
        except HTTPError as exc:
            if exc.code in (403, 567):
                raise FetchError(
                    f"AI HOT rejected the request ({exc.code}); check the identifying User-Agent"
                ) from exc
            if exc.code == 429 and attempt < retries - 1:
                retry_after = exc.headers.get("Retry-After", "30")
                try:
                    delay = min(60.0, max(1.0, float(retry_after)))
                except ValueError:
                    delay = 30.0
                time.sleep(delay + random.random())
                continue
            if 500 <= exc.code < 600 and attempt < retries - 1:
                time.sleep((2**attempt) + random.random())
                continue
            raise FetchError(f"AI HOT returned HTTP {exc.code} for {path}") from exc
        except (URLError, TimeoutError, json.JSONDecodeError) as exc:
            if attempt < retries - 1:
                time.sleep((2**attempt) + random.random())
                continue
            raise FetchError(f"Unable to fetch valid JSON from {path}: {exc}") from exc

    raise FetchError(f"Unable to fetch {path}")


def fingerprint_value(payload: dict[str, Any]) -> str:
    # We fetch mode=selected, so unrelated changes in the full firehose must not
    # trigger a rewrite or deployment.
    for key in ("selected", "fingerprint", "value", "hash", "etag", "version", "all"):
        value = payload.get(key)
        if value not in (None, ""):
            return str(value)
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    attribution = item.get("attribution") if isinstance(item.get("attribution"), dict) else {}
    score = item.get("score")
    try:
        source_score = float(score) if score is not None else None
    except (TypeError, ValueError):
        source_score = None

    return {
        "id": str(item.get("id") or item.get("permalink") or item.get("url") or ""),
        "channel": "aihot",
        "title": str(item.get("title") or item.get("title_en") or "未命名动态").strip(),
        "title_en": str(item.get("title_en") or "").strip(),
        "summary": str(item.get("summary") or "").strip(),
        "source": str(item.get("source") or attribution.get("source") or "AI HOT").strip(),
        "published_at": str(item.get("publishedAt") or item.get("published_at") or ""),
        "category": str(item.get("category") or "AI 动态").strip(),
        "source_score": source_score,
        "selected": bool(item.get("selected")),
        "permalink": str(item.get("permalink") or attribution.get("canonical") or "").strip(),
        "original_url": str(item.get("url") or "").strip(),
        "attribution": {
            "source": str(attribution.get("source") or "AI HOT").strip(),
            "canonical": str(attribution.get("canonical") or item.get("permalink") or "").strip(),
        },
    }


def merge_archive(existing: dict[str, Any], items: list[dict[str, Any]], fetched_at: str) -> dict[str, Any]:
    merged: dict[str, dict[str, Any]] = {}
    old_items = existing.get("items", []) if isinstance(existing, dict) else []
    for item in old_items:
        if isinstance(item, dict) and item.get("id"):
            merged[str(item["id"])] = item
    for item in items:
        if item.get("id"):
            merged[str(item["id"])] = item

    def sort_key(item: dict[str, Any]) -> str:
        return str(item.get("published_at") or "")

    return {
        "schema_version": 1,
        "updated_at": fetched_at,
        "count": len(merged),
        "items": sorted(merged.values(), key=sort_key, reverse=True),
    }


def write_outputs(snapshot: dict[str, Any], archive: dict[str, Any]) -> None:
    json_text = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    archive_text = json.dumps(archive, ensure_ascii=False, indent=2) + "\n"
    js_text = "window.AIHOT_FEED = " + json.dumps(
        snapshot, ensure_ascii=False, separators=(",", ":")
    ) + ";\n"
    atomic_write(SNAPSHOT_PATH, json_text)
    atomic_write(ARCHIVE_PATH, archive_text)
    atomic_write(JS_PATH, js_text)
    if INDEX_PATH.exists():
        index_html = INDEX_PATH.read_text(encoding="utf-8")
        version = re.sub(r"\D", "", str(snapshot.get("fetched_at") or ""))[:14]
        refreshed = re.sub(
            r'<script src="aihot\.js(?:\?v=[^"]*)?"></script>',
            f'<script src="aihot.js?v={version}"></script>',
            index_html,
            count=1,
        )
        if refreshed != index_html:
            atomic_write(INDEX_PATH, refreshed)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch AI HOT public items for Sequentry Atlas")
    parser.add_argument("--force", action="store_true", help="Fetch even when the fingerprint is unchanged")
    parser.add_argument("--take", type=int, default=50, help="Selected items to fetch (1-100)")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds")
    parser.add_argument(
        "--user-agent",
        default=os.getenv("AIHOT_USER_AGENT", DEFAULT_UA),
        help="Identifying User-Agent required by the public API",
    )
    args = parser.parse_args()
    take = min(100, max(1, args.take))

    previous = read_json(SNAPSHOT_PATH, {})
    try:
        fingerprint_payload, fingerprint_headers = request_json(
            "/fingerprint", params=None, user_agent=args.user_agent, timeout=args.timeout
        )
        fingerprint = fingerprint_value(fingerprint_payload)

        if not args.force and previous.get("fingerprint") == fingerprint:
            print(f"AI HOT unchanged ({fingerprint}); retained existing snapshot")
            return 0

        items_payload, _ = request_json(
            "/items",
            params={"mode": "selected", "take": take},
            user_agent=args.user_agent,
            timeout=args.timeout,
        )
        hot_topics_payload, _ = request_json(
            "/hot-topics", params=None, user_agent=args.user_agent, timeout=args.timeout
        )
        daily_payload, _ = request_json(
            "/daily", params=None, user_agent=args.user_agent, timeout=args.timeout
        )
    except FetchError as exc:
        if previous.get("items"):
            print(f"AI HOT unavailable; retained stale snapshot: {exc}", file=sys.stderr)
            return 0
        print(f"AI HOT fetch failed and no cache exists: {exc}", file=sys.stderr)
        return 1

    raw_items = items_payload.get("items", [])
    items = [normalize_item(item) for item in raw_items if isinstance(item, dict)]
    items = [item for item in items if item["id"] and item["title"]]
    fetched_at = now_iso()
    snapshot = {
        "schema_version": 1,
        "provider": "AI HOT",
        "provider_url": "https://aihot.virxact.com/",
        "api_version": fingerprint_headers.get("x-api-version", ""),
        "fingerprint": fingerprint,
        "fetched_at": fetched_at,
        "stale": False,
        "count": len(items),
        "items": items,
        "hot_topics": hot_topics_payload.get("topics", hot_topics_payload.get("items", [])),
        "daily": daily_payload,
    }
    archive = merge_archive(read_json(ARCHIVE_PATH, {}), items, fetched_at)
    write_outputs(snapshot, archive)
    print(f"AI HOT updated: {len(items)} selected items; fingerprint {fingerprint}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
