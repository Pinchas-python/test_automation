"""
Login Page Object
Contains locators and methods specific to the login page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):
    # Locators for Bio-Beat login page
    USERNAME_INPUT = "input[placeholder='Username']"
    PASSWORD_INPUT = "input[placeholder='Password']"
    LOGIN_BUTTON = "button[type='submit']:has-text('Login')"
    ERROR_MESSAGE = "[role='alert'], .amplify-alert, .error, [class*='error'], [class*='alert']"
    SUCCESS_MESSAGE = ".success-message, [class*='success']"
    LOGOUT_BUTTON = "button:has-text('Logout'), button:has-text('Sign out')"
    FORGOT_PASSWORD_LINK = "button:has-text('Forgot your password?')"
    USERNAME_LABEL = "label:has-text('Username')"
    PASSWORD_LABEL = "label:has-text('Password')"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    def navigate_to_login(self, base_url: str):
        """Navigate to login page"""
        self.navigate_to(base_url)
    
    def enter_username(self, username: str):
        """Enter username in the username field"""
        self.fill(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """Enter password in the password field"""
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """Click the login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self) -> str:
        """Get error message text"""
        self.wait_for_selector(self.ERROR_MESSAGE, timeout=5000)
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is visible"""
        try:
            # Wait a moment for error to appear
            self.page.wait_for_timeout(1000)
            # Check for Mui-error class on inputs (Bio-Beat specific)
            error_elements = self.page.locator(".Mui-error")
            return error_elements.count() > 0
        except:
            return False
    
    def is_logged_in(self) -> bool:
        """Check if user is logged in (logout button is visible)"""
        try:
            return self.is_visible(self.LOGOUT_BUTTON)
        except:
            return False
