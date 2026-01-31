"""
Login Tests
Tests for login functionality with various scenarios
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLogin:
    """Test cases for login functionality"""
    
    def test_login_with_wrong_username(self, page):
        """Test login with incorrect username"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with wrong username
        login_page.login("wronguser@example.com", Config.VALID_PASSWORD)
        
        # Verify error message is displayed
        assert login_page.is_error_displayed(), "Error message should be displayed"
        # Optionally verify the error message content
        # error_text = login_page.get_error_message()
        # assert "Invalid credentials" in error_text or "incorrect" in error_text.lower()
    
    def test_login_with_wrong_password(self, page):
        """Test login with incorrect password"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with wrong password
        login_page.login(Config.VALID_USERNAME, "WrongPassword123!")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed(), "Error message should be displayed"
    
    def test_login_with_empty_username(self, page):
        """Test login with empty username"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with empty username
        login_page.login("", Config.VALID_PASSWORD)
        
        # Verify error message is displayed
        assert login_page.is_error_displayed(), "Error message should be displayed for empty username"
    
    def test_login_with_empty_password(self, page):
        """Test login with empty password"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with empty password
        login_page.login(Config.VALID_USERNAME, "")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed(), "Error message should be displayed for empty password"
    
    def test_login_with_both_empty(self, page):
        """Test login with both username and password empty"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with both fields empty
        login_page.login("", "")
        
        # Verify error message is displayed
        assert login_page.is_error_displayed(), "Error message should be displayed when both fields are empty"
    
    @pytest.mark.skip(reason="Add valid credentials to test successful login")
    def test_login_with_valid_credentials(self, page):
        """Test login with valid credentials"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Login with valid credentials
        login_page.login(Config.VALID_USERNAME, Config.VALID_PASSWORD)
        
        # Verify user is logged in
        assert login_page.is_logged_in(), "User should be logged in successfully"
