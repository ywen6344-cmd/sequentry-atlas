$ErrorActionPreference = 'Stop'

$atlas = $PSScriptRoot
$desktop = [Environment]::GetFolderPath('Desktop')
$collector = Get-ChildItem -LiteralPath $desktop -Directory -ErrorAction SilentlyContinue |
    ForEach-Object {
        $candidate = Join-Path $_.FullName 'feed-collectors-v2'
        if (Test-Path -LiteralPath (Join-Path $candidate 'run_daily.ps1')) {
            Get-Item -LiteralPath $candidate
        }
    } |
    Select-Object -First 1

if (-not $collector) {
    Write-Error 'feed-collectors-v2 was not found under Desktop.'
    exit 1
}

$collectorRoot = $collector.FullName
$collectorPython = Join-Path $collectorRoot '.venv\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $collectorPython)) {
    Write-Error "Collector Python was not found: $collectorPython"
    exit 1
}

Write-Host '[1/2] Refreshing cross-border sources...'
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File (Join-Path $collectorRoot 'run_daily.ps1')
if ($LASTEXITCODE -ne 0) {
    Write-Error "Collector refresh failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}

Write-Host '[2/2] Refreshing AI news and rebuilding Atlas pages...'
& $collectorPython (Join-Path $atlas 'update_content.py')
if ($LASTEXITCODE -ne 0) {
    Write-Error "Atlas refresh failed with exit code $LASTEXITCODE"
    exit $LASTEXITCODE
}

Write-Host 'Done. Local data and pages are up to date.' -ForegroundColor Green
Write-Host 'This command does not publish the Atlas website.'
