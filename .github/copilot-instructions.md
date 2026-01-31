# AI Agent Instructions - Playwright Python Test Automation Framework

## Project Overview
Playwright Python test automation framework using Page Object Model (POM) pattern for testing Bio-Beat's staging environment (`https://bpholter.stage.bio-beat.cloud`). Framework emphasizes modular design with session-scoped browser fixtures and function-scoped page contexts.

## Architecture

### Page Object Model Structure
- **BasePage** ([pages/base_page.py](pages/base_page.py)): Core page methods inherited by all page objects. Wraps Playwright's `page.locator()` pattern.
- **Page Objects** (e.g., [pages/login_page.py](pages/login_page.py)): Define locators as class constants (e.g., `USERNAME_INPUT = "input[name='username']"`) and business methods. Always inherit from `BasePage`.
- **Test Classes**: Organize related tests in classes (e.g., `TestLogin`, `TestLoginSecurity`). Use `LoginPage(page)` instantiation pattern in each test method.

### Fixture Hierarchy (conftest.py)
Critical fixture scoping pattern:
```python
playwright_instance (session) → browser (session) → context (function) → page (function)
```
- **Browser** launched once per test session for speed
- **Context** created per test for isolation (viewport, timeouts, video recording)
- **Page** is function-scoped; always use `page` fixture parameter, never create manually
- Screenshot on failure auto-triggers via `screenshot_on_failure` fixture + `pytest_runtest_makereport` hook

## Key Conventions

### Test Organization & Markers
Use pytest markers from [pytest.ini](pytest.ini#L8-L12):
- `@pytest.mark.smoke` - Quick critical path tests
- `@pytest.mark.validation` - Input validation tests
- `@pytest.mark.security` - Security tests (SQL injection, XSS)
- `@pytest.mark.ui` - UI verification tests
- Run: `py -m pytest -m smoke -v`

### Configuration Management
All test settings in [config/config.py](config/config.py):
- `BASE_URL`: Target environment (currently Bio-Beat staging)
- `HEADLESS = False`: Framework runs headed by default for debugging
- `DEFAULT_TIMEOUT = 30000`: Applied to all context operations via `context.set_default_timeout()`
- Update locators in page objects when testing different sites, NOT in config

### Locator Strategy
**Multiple fallback selectors** pattern for robustness:
```python
ERROR_MESSAGE = "[role='alert'], .amplify-alert, .error, [class*='error']"
LOGIN_BUTTON = "button:has-text('Login')"
```
Use Playwright's auto-waiting; explicit `wait_for_selector()` only for async operations.

## Developer Workflows

### Running Tests (Windows)
**Always use** `py -m pytest` (not `pytest` alone) to ensure correct interpreter:
```powershell
# Run all tests
py -m pytest

# Run specific file with verbose output
py -m pytest tests/test_validation.py -v

# Run specific test method
py -m pytest tests/test_login.py::TestLogin::test_login_with_wrong_username -v

# Run by marker
py -m pytest -m smoke -v

# Parallel execution (faster)
py -m pytest -n auto

# Generate HTML report
py -m pytest --html=report.html --self-contained-html
```

### Running Tests in Docker
Build and run tests in containerized environment with Allure reports:
```powershell
# Build Docker image
docker build -t playwright-tests .

# Run all tests with Allure results
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests

# View Allure report
allure serve allure-results

# Run specific test
docker run --rm -v ${PWD}/allure-results:/app/allure-results playwright-tests xvfb-run pytest tests/test_login.py::TestLogin::test_login_with_wrong_username -v --alluredir=/app/allure-results
```
- **Docker image**: `mcr.microsoft.com/playwright/python:v1.57.0-noble`
- Uses `xvfb` for headless execution
- See [DOCKER.md](DOCKER.md) for detailed Docker instructions

## GitHub Actions CI/CD

Tests automatically run on push/PR via GitHub Actions workflow ([.github/workflows/playwright-tests.yml](.github/workflows/playwright-tests.yml)):
- Runs on `ubuntu-latest` with Python 3.11
- Generates Allure reports published to GitHub Pages
- Uploads failure screenshots as artifacts (7-day retention)
- Triggers on push to main/master/develop branches and PRs
- Manual trigger available via workflow_dispatch

View reports at: `https://<username>.github.io/<repo>/`

### Enabling GitHub Pages
1. Go to repository Settings → Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages` / `root`
4. Save - reports will be available after first workflow run

### Running Tests in Docker
For consistent CI/CD environment:
```powershell
# Quick run with automated script
.\run-tests-docker.ps1

# Or using docker-compose directly
docker-compose run --rm playwright-tests

# Run specific tests in Docker
docker-compose run --rm playwright-tests pytest tests/test_login.py -v
```

### VS Code Test Explorer
1. Open Testing Panel (🧪 icon or `Ctrl+Shift+T`)
2. Click refresh if tests don't appear
3. Use ▶️ to run, 🐛 to debug with breakpoints
4. Failed test screenshots auto-save to [screenshots/](screenshots/) with timestamp

### Debugging Failed Tests
1. Check `screenshots/` directory for failure screenshots (named `{test_name}_{timestamp}.png`)
2. Set `HEADLESS = False` in config to watch browser
3. Set `SLOW_MO = 500` to slow down actions
4. Use VS Code debugger with breakpoints in page objects or tests

## Adding New Tests

### Creating a New Page Object
```python
from pages.base_page import BasePage
from playwright.sync_api import Page

class DashboardPage(BasePage):
    # Define locators as class constants
    WELCOME_MESSAGE = "h1.welcome"
    USER_MENU = "[data-testid='user-menu']"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_welcome_text(self) -> str:
        """Business method using BasePage.get_text()"""
        return self.get_text(self.WELCOME_MESSAGE)
```

### Writing Tests
Follow existing patterns:
- Import page objects and `Config`
- Organize in test classes for grouping
- Use descriptive docstrings
- Instantiate page objects: `login_page = LoginPage(page)`
- Navigate, interact, assert
- Apply appropriate markers

Example:
  - Username/Password inputs use `placeholder` attributes: `input[placeholder='Username']`
  - Error detection uses `.Mui-error` class (Material-UI framework)
  - Login page is at root URL, not `/login` path
- **Timeouts**: 30s default sufficient for most cases; increase `Config.NAVIGATION_TIMEOUT` if testing slow-loading pages
- **Error handling**: Page object methods use try/except for `is_visible()` checks to return False instead of raising
- **Test data**: Update `VALID_USERNAME`/`VALID_PASSWORD` in config for successful login tests (currently using example values)
- **Docker**: Use `docker-compose run --rm playwright-tests` for CI/CD environments (see [DOCKER.md](DOCKER.md)
    def test_welcome_message_displayed(self, page):
        """Verify welcome message appears after login"""
        dashboard = DashboardPage(page)
        dashboard.navigate_to(Config.BASE_URL)
        assert dashboard.is_visible(dashboard.WELCOME_MESSAGE)
```

## Critical Details
- **Never modify fixture scopes** in conftest.py - breaks test isolation
- **Bio-Beat specific**: Tests currently use Bio-Beat staging locators; update `LoginPage` locators for new sites
- **Timeouts**: 30s default sufficient for most cases; increase `Config.NAVIGATION_TIMEOUT` if testing slow-loading pages
- **Error handling**: Page object methods use try/except for `is_visible()` checks to return False instead of raising
- **Test data**: Update `VALID_USERNAME`/`VALID_PASSWORD` in config for successful login tests (currently using example values)
