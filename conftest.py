"""
Pytest configuration and fixtures
"""
import pytest
import os
import requests
from playwright.sync_api import Page, BrowserContext
from config.config import Config
from datetime import datetime


def pytest_collection_modifyitems(config, items):
    """Skip all tests if site is not accessible in CI environment"""
    is_ci = os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'
    
    if is_ci:
        try:
            response = requests.get(Config.BASE_URL, timeout=10)
            if response.status_code not in [200, 301, 302]:
                skip_marker = pytest.mark.skip(reason=f"Test site {Config.BASE_URL} is not accessible (HTTP {response.status_code})")
                for item in items:
                    item.add_marker(skip_marker)
        except Exception as e:
            skip_marker = pytest.mark.skip(reason=f"Test site {Config.BASE_URL} is not accessible: {str(e)}")
            for item in items:
                item.add_marker(skip_marker)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context with custom settings"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser launch arguments"""
    # Force headless mode in CI environments
    is_ci = os.getenv('CI') == 'true' or os.getenv('GITHUB_ACTIONS') == 'true'
    headless = True if is_ci else Config.HEADLESS
    
    return {
        **browser_type_launch_args,
        "headless": headless,
        "slow_mo": Config.SLOW_MO,
    }


@pytest.fixture(scope="function")
def context(context: BrowserContext):
    """Configure context with timeouts"""
    context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    context.set_default_navigation_timeout(Config.NAVIGATION_TIMEOUT)
    yield context


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Page):
    """Take screenshot on test failure"""
    yield
    if request.node.rep_call.failed if hasattr(request.node, 'rep_call') else False:
        if Config.SCREENSHOT_ON_FAILURE:
            os.makedirs(Config.SCREENSHOT_PATH, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{request.node.name}_{timestamp}.png"
            screenshot_path = os.path.join(Config.SCREENSHOT_PATH, screenshot_name)
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results for screenshot fixture"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
