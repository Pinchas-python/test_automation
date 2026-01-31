"""
Base Page class that all page objects will inherit from
Contains common methods used across all pages
"""
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get the page title"""
        return self.page.title()
    
    def click(self, locator: str):
        """Click on an element"""
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str):
        """Fill input field with text"""
        self.page.locator(locator).fill(text)
    
    def get_text(self, locator: str) -> str:
        """Get text content of an element"""
        return self.page.locator(locator).text_content()
    
    def is_visible(self, locator: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(locator).is_visible()
    
    def wait_for_selector(self, locator: str, timeout: int = 30000):
        """Wait for element to be visible"""
        self.page.wait_for_selector(locator, timeout=timeout)
    
    def take_screenshot(self, filename: str):
        """Take a screenshot"""
        self.page.screenshot(path=filename)
    
    def get_url(self) -> str:
        """Get current URL"""
        return self.page.url
