#!/usr/bin/env python3
"""Refresh all Atlas content snapshots in deployment order.

This is the single command for CI or Windows Task Scheduler. AI HOT performs a
fingerprint check internally, so frequent runs do not create noisy file changes.
"""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUTS = (
    ROOT / "feed.js",
    ROOT / "aihot.js",
    ROOT / "data" / "commerce.json",
    ROOT / "data" / "aihot.json",
    ROOT / "data" / "aihot_archive.json",
    ROOT / "briefs" / "index.html",
    ROOT / "index.html",
)


def digest(path: Path) -> str:
    if not path.exists():
        return ""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(script: str, *args: str) -> None:
    command = [sys.executable, str(ROOT / script), *args]
    completed = subprocess.run(command, cwd=ROOT, check=False)
    if completed.returncode:
        raise SystemExit(completed.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(description="Refresh Sequentry Atlas content")
    parser.add_argument("--force-aihot", action="store_true", help="Ignore the saved AI HOT fingerprint")
    parser.add_argument("--skip-commerce", action="store_true", help="Do not rebuild from briefing.json")
    args = parser.parse_args()

    before = {path: digest(path) for path in OUTPUTS}
    if not args.skip_commerce:
        run("build_feed.py")
    run("fetch_aihot.py", *( ["--force"] if args.force_aihot else [] ))
    run("build_briefs.py")
    changed = [path.relative_to(ROOT) for path in OUTPUTS if before[path] != digest(path)]

    if changed:
        print("changed:")
        for path in changed:
            print(f"  {path}")
    else:
        print("changed: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
