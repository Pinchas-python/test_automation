# Playwright Python Test Automation Framework

A modular test automation framework using Playwright with Python and the Page Object Model (POM) design pattern.

## 📁 Project Structure

```
test automation/
├── config/
│   └── config.py          # Configuration settings (URLs, credentials, timeouts)
├── pages/
│   ├── base_page.py       # Base page with common methods
│   └── login_page.py      # Login page object
├── tests/
│   ├── test_login.py              # Login test cases
│   └── test_login_extended.py     # Additional login tests
├── conftest.py            # Pytest fixtures and hooks
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 2. Configure Your Tests

Edit [config/config.py](config/config.py) to set:
- `BASE_URL`: Your website URL
- `VALID_USERNAME` and `VALID_PASSWORD`: Valid credentials (if testing successful login)
- Browser settings (headless mode, timeouts, etc.)

### 3. Update Page Locators

Edit [pages/login_page.py](pages/login_page.py) to match your website's actual element locators:
- Inspect your login page elements
- Update the locator strings (CSS selectors, XPath, etc.)

## 🧪 Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_login.py
```

### Run specific test
```bash
pytest tests/test_login.py::TestLogin::test_login_with_wrong_username
```

### Run with HTML report
```bash
pytest --html=report.html --self-contained-html
```

### Run in headed mode (see browser)
Update `HEADLESS = False` in [config/config.py](config/config.py)

### Run with specific markers
```bash
pytest -m security  # Run only security tests
pytest -m ui        # Run only UI tests
```

### Run tests in parallel
```bash
pytest -n auto  # Use all available CPU cores
pytest -n 4     # Use 4 workers
```

## 📝 Writing New Tests

### 1. Create a New Page Object

Create a new file in `pages/` directory:

```python
from pages.base_page import BasePage
from playwright.sync_api import Page

class DashboardPage(BasePage):
    # Define locators
    WELCOME_MESSAGE = "h1.welcome"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_welcome_message(self) -> str:
        return self.get_text(self.WELCOME_MESSAGE)
```

### 2. Create a New Test File

Create a new file in `tests/` directory:

```python
import pytest
from pages.dashboard_page import DashboardPage
from config.config import Config

class TestDashboard:
    def test_dashboard_loads(self, page):
        dashboard = DashboardPage(page)
        dashboard.navigate_to(f"{Config.BASE_URL}/dashboard")
        assert "Welcome" in dashboard.get_welcome_message()
```

## 🎯 Best Practices

1. **Page Object Model**: Keep page elements and methods in page objects
2. **DRY Principle**: Use base page for common methods
3. **Fixtures**: Use pytest fixtures for setup/teardown
4. **Assertions**: Use clear, descriptive assertions
5. **Markers**: Use pytest markers to organize tests (@pytest.mark.smoke, @pytest.mark.regression)
6. **Screenshots**: Automatic screenshots on failure (configured in conftest.py)

## � Docker Support

Run tests in Docker containers with Allure reporting:

```bash
# Build image
docker build -t playwright-tests .

# Run tests
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests

# View report
allure serve allure-results
```

See [DOCKER.md](DOCKER.md) for complete Docker instructions.

## 🚀 CI/CD with GitHub Actions

Tests automatically run on every push and pull request:
- Automated test execution on Ubuntu
- Allure reports published to GitHub Pages
- Screenshots uploaded as artifacts on failure

View live reports at: `https://<your-username>.github.io/<repo-name>/`

To enable GitHub Pages:
1. Go to repository Settings → Pages
2. Set Source to "Deploy from a branch"
3. Select `gh-pages` branch
4. Save and wait for the first workflow run

## �📊 Test Coverage

Current test scenarios:
- ✅ Login with wrong username
- ✅ Login with wrong password
- ✅ Login with empty username
- ✅ Login with empty password
- ✅ Login with both fields empty
- ✅ SQL injection prevention
- ✅ XSS prevention
- ✅ UI element visibility

## 🔧 Configuration Options

Available in [config/config.py](config/config.py):
- Browser type (chromium, firefox, webkit)
- Headless mode
- Timeouts
- Screenshot settings
- Video recording

## 📚 Resources

- [Playwright Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://playwright.dev/python/docs/pom)
