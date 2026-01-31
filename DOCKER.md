# Docker Setup for Playwright Tests

## Build Docker Image

```powershell
docker build -t playwright-tests .
```

## Run Tests with Allure Reports

### Run all tests and generate Allure results:
```powershell
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests
```

### View Allure report:
```powershell
allure serve allure-results
```

## Run Specific Tests

### Run specific test file:
```powershell
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests xvfb-run pytest tests/test_login.py -v --alluredir=/app/allure-results
```

### Run specific test:
```powershell
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests xvfb-run pytest tests/test_login.py::TestLogin::test_login_with_wrong_username -v --alluredir=/app/allure-results
```

### Run with markers:
```powershell
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests xvfb-run pytest -m smoke -v --alluredir=/app/allure-results
```

## Save Screenshots and Videos

```powershell
docker run --rm -v ${PWD}/allure-results:/app/allure-results -v ${PWD}/screenshots:/app/screenshots -v ${PWD}/videos:/app/videos playwright-tests
```

## Prerequisites for Allure Reports

To view Allure reports, install Allure CLI:

### Windows (using Scoop):
```powershell
scoop install allure
```

### Windows (using Chocolatey):
```powershell
choco install allure
```

### Or download manually from:
https://github.com/allure-framework/allure2/releases

## Image Details

- Base Image: `mcr.microsoft.com/playwright/python:v1.57.0-noble`
- Includes xvfb for headless browser execution
- Pre-configured with all dependencies from requirements.txt
