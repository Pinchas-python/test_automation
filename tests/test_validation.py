"""
Validation Tests for User and Password Fields
Tests specific to Bio-Beat login page validation
"""
import pytest
from pages.login_page import LoginPage
from config.config import Config


class TestLoginFieldValidation:
    """Validation tests for username and password fields"""
    
    def test_username_field_exists(self, page):
        """Test that username field is present on the page"""
        login_page = LoginPage(page)
        login_page.navigate_to_login(Config.BASE_URL)
        
        # Verify username field exists and is visible
        assert login_page.is_visible(login_page.USERNAME_INPUT), "Username field should be visible"
        assert login_page.is_visible(login_page.USERNAME_LABEL), "Username label should be visible"
    
#     def test_password_field_exists(self, page):
#         """Test that password field is present on the page"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Verify password field exists and is visible
#         assert login_page.is_visible(login_page.PASSWORD_INPUT), "Password field should be visible"
#         assert login_page.is_visible(login_page.PASSWORD_LABEL), "Password label should be visible"
    
#     @pytest.mark.smoke
#     def test_password_field_is_masked(self, page):
#         """Test that password field input is masked"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Get password input type attribute
#         input_type = page.locator(login_page.PASSWORD_INPUT).get_attribute("type")
#         assert input_type == "password", f"Password field should be masked, but type is: {input_type}"
    
#     @pytest.mark.smoke
#     def test_username_accepts_input(self, page):
#         """Test that username field accepts text input"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         test_username = "test.user@example.com"
#         login_page.enter_username(test_username)
        
#         # Verify input was accepted
#         value = page.locator(login_page.USERNAME_INPUT).input_value()
#         assert value == test_username, f"Username field should contain '{test_username}', got '{value}'"
    
#     @pytest.mark.smoke
#     def test_password_accepts_input(self, page):
#         """Test that password field accepts text input"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         test_password = "TestPassword123!"
#         login_page.enter_password(test_password)
        
#         # Verify input was accepted
#         value = page.locator(login_page.PASSWORD_INPUT).input_value()
#         assert value == test_password, f"Password field should contain the entered text"
    
#     @pytest.mark.validation
#     def test_username_field_required(self, page):
#         """Test validation when username is empty"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Try to login with empty username
#         login_page.enter_password("SomePassword123")
#         login_page.click_login_button()
        
#         # Should show validation error or prevent submission
#         # Note: Adjust assertion based on actual behavior
#         assert True, "Username field validation should trigger"
    
#     @pytest.mark.validation
#     def test_password_field_required(self, page):
#         """Test validation when password is empty"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Try to login with empty password
#         login_page.enter_username("test@example.com")
#         login_page.click_login_button()
        
#         # Should show validation error or prevent submission
#         assert True, "Password field validation should trigger"
    
#     @pytest.mark.validation
#     def test_username_special_characters(self, page):
#         """Test username field with special characters"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         special_username = "user+test@example.com"
#         login_page.enter_username(special_username)
        
#         value = page.locator(login_page.USERNAME_INPUT).input_value()
#         assert value == special_username, "Username field should accept special characters"
    
#     @pytest.mark.validation
#     def test_password_special_characters(self, page):
#         """Test password field with special characters"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         special_password = "P@ssw0rd!#$%"
#         login_page.enter_password(special_password)
        
#         value = page.locator(login_page.PASSWORD_INPUT).input_value()
#         assert value == special_password, "Password field should accept special characters"
    
#     @pytest.mark.validation
#     def test_username_max_length(self, page):
#         """Test username field with very long input"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         long_username = "a" * 300  # Very long username
#         login_page.enter_username(long_username)
        
#         value = page.locator(login_page.USERNAME_INPUT).input_value()
#         assert len(value) > 0, "Username field should accept input (may truncate)"
    
#     @pytest.mark.validation
#     def test_password_spaces(self, page):
#         """Test password field with spaces"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         password_with_spaces = "Pass word 123"
#         login_page.enter_password(password_with_spaces)
        
#         value = page.locator(login_page.PASSWORD_INPUT).input_value()
#         assert value == password_with_spaces, "Password field should accept spaces"
    
#     @pytest.mark.validation
#     def test_fields_clear_on_error(self, page):
#         """Test if fields remain or clear after login error"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         test_username = "wrong@example.com"
#         test_password = "WrongPassword"
        
#         login_page.login(test_username, test_password)
        
#         # Check if fields retain values or are cleared
#         username_value = page.locator(login_page.USERNAME_INPUT).input_value()
#         password_value = page.locator(login_page.PASSWORD_INPUT).input_value()
        
#         # This behavior depends on the application design
#         # Document the actual behavior
#         print(f"After failed login - Username: {'retained' if username_value else 'cleared'}, Password: {'retained' if password_value else 'cleared'}")
    
#     @pytest.mark.smoke
#     @pytest.mark.ui
#     def test_login_button_enabled(self, page):
#         """Test that login button is initially enabled"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Check if login button is enabled
#         is_enabled = page.locator(login_page.LOGIN_BUTTON).is_enabled()
#         assert is_enabled, "Login button should be enabled"
    
#     @pytest.mark.ui
#     def test_forgot_password_link_exists(self, page):
#         """Test that 'Forgot Password' link is present"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Check if forgot password link exists
#         assert login_page.is_visible(login_page.FORGOT_PASSWORD_LINK), "Forgot password link should be visible"


# @pytest.mark.validation
# class TestLoginWithInvalidCredentials:
#     """Tests for various invalid credential scenarios"""
    
#     @pytest.mark.smoke
#     @pytest.mark.parametrize("username,password,description", [
#         ("invalid@example.com", "WrongPass123", "Invalid username with valid password format"),
#         ("validuser@example.com", "wrong", "Valid username format with invalid password"),
#         ("notanemail", "Password123", "Username without @ symbol"),
#         ("user@", "Password123", "Incomplete email address"),
#         ("@example.com", "Password123", "Email without username part"),
#         ("user name@example.com", "Password123", "Email with space in username"),
#         ("admin", "admin", "Common default credentials"),
#         ("test", "test", "Simple test credentials"),
#     ])
#     def test_invalid_credentials_combinations(self, page, username, password, description):
#         """Test login with various invalid credential combinations"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.login(username, password)
        
#         # Should show error or prevent login
#         # Check that user is not logged in
#         assert not login_page.is_logged_in(), f"Should not log in with: {description}"
    
#     @pytest.mark.validation
#     def test_numeric_username(self, page):
#         """Test login with numeric username"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.login("12345", "Password123")
        
#         # Verify error is shown
#         assert login_page.is_error_displayed() or not login_page.is_logged_in(), \
#             "Numeric username should not be accepted"
    
#     @pytest.mark.validation
#     def test_very_short_password(self, page):
#         """Test login with very short password"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.login("user@example.com", "123")
        
#         # Should show error
#         assert login_page.is_error_displayed() or not login_page.is_logged_in(), \
#             "Very short password should be rejected"
    
#     @pytest.mark.validation
#     def test_username_with_leading_trailing_spaces(self, page):
#         """Test username with leading/trailing spaces"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.login("  user@example.com  ", "Password123")
        
#         # Should either trim spaces or show error
#         assert not login_page.is_logged_in(), "Login with spaces should fail"
    
#     @pytest.mark.validation
#     def test_case_sensitive_username(self, page):
#         """Test if username is case sensitive"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.login("USER@EXAMPLE.COM", "Password123")
        
#         # Document whether username is case sensitive
#         print("Test case sensitivity of username field")


# @pytest.mark.smoke
# @pytest.mark.ui
# class TestLoginButtonBehavior:
#     """Tests for login button behavior and states"""
    
#     @pytest.mark.smoke
#     def test_login_button_text(self, page):
#         """Test that login button has correct text"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         button_text = page.locator(login_page.LOGIN_BUTTON).inner_text()
#         assert "login" in button_text.lower(), f"Login button should contain 'Login', got: {button_text}"
    
#     @pytest.mark.smoke
#     def test_login_button_clickable(self, page):
#         """Test that login button is clickable"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         # Fill fields
#         login_page.enter_username("test@example.com")
#         login_page.enter_password("TestPass123")
        
#         # Click should not throw error
#         login_page.click_login_button()
#         assert True, "Login button should be clickable"
    
#     @pytest.mark.ui
#     def test_enter_key_submits_form(self, page):
#         """Test that pressing Enter in password field submits form"""
#         login_page = LoginPage(page)
#         login_page.navigate_to_login(Config.BASE_URL)
        
#         login_page.enter_username("test@example.com")
#         login_page.enter_password("TestPass123")
        
#         # Press Enter in password field
#         page.locator(login_page.PASSWORD_INPUT).press("Enter")
        
#         # Should trigger login attempt
#         page.wait_for_timeout(1000)  # Wait for form submission
#         assert True, "Enter key should submit the login form"
