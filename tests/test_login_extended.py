"""
Example of additional test file
You can create more test files following this pattern
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLoginSecurity:
    """Security-related tests for login"""
    
    @pytest.mark.security
    def test_sql_injection_in_username(self, page):
        """Test SQL injection attempt in username field"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Try SQL injection
        login_page.login("admin' OR '1'='1", Config.VALID_PASSWORD)
        
        # Should show error, not allow login
        assert login_page.is_error_displayed(), "SQL injection should be prevented"
    
    @pytest.mark.security
    def test_xss_in_username(self, page):
        """Test XSS attempt in username field"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Try XSS injection
        login_page.login("<script>alert('XSS')</script>", Config.VALID_PASSWORD)
        
        # Should show error, not execute script
        assert login_page.is_error_displayed(), "XSS should be prevented"


class TestLoginUI:
    """UI-related tests for login page"""
    
    @pytest.mark.ui
    def test_login_page_title(self, page):
        """Test login page has correct title"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        title = login_page.get_title()
        assert "bio" in title.lower() or "login" in title.lower(), f"Page title should contain 'Biobeat' or 'login', got: {title}"
    
    @pytest.mark.ui
    def test_login_page_elements_visible(self, page):
        """Test all login page elements are visible"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Verify key elements are visible
        assert login_page.is_visible(login_page.USERNAME_INPUT), "Username field should be visible"
        assert login_page.is_visible(login_page.PASSWORD_INPUT), "Password field should be visible"
        assert login_page.is_visible(login_page.LOGIN_BUTTON), "Login button should be visible"
