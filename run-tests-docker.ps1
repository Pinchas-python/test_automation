# PowerShell script to run Playwright tests in Docker

Write-Host "Running Playwright tests in Docker..." -ForegroundColor Green

# Pull the latest Playwright image
Write-Host "`nPulling Playwright Docker image..." -ForegroundColor Yellow
docker pull mcr.microsoft.com/playwright:v1.58.0-noble

# Run tests using docker-compose
Write-Host "`nRunning tests..." -ForegroundColor Yellow
docker-compose run --rm playwright-tests

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host "`nTests completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`nTests failed with exit code: $LASTEXITCODE" -ForegroundColor Red
}

# Copy results
Write-Host "`nTest results and screenshots are available in the current directory" -ForegroundColor Cyan
