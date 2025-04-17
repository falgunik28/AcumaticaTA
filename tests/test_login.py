import pytest
import json
from tests import file_path
from pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load JSON test data
with open(file_path) as file:
    data = json.load(file)

# Test cases using values from JSON
test_data = [
     (data["valid_user"], data["valid_password"], "Hi Practice"),  # Valid Login
     (data["valid_user"], data["invalid_password"], "Your password is invalid!"),  # Invalid password
     (data["invalid_username"], data["valid_password"], "Your username is invalid!"),  # Invalid username
     (data["invalid_username"], data["invalid_password"], "Your username is invalid!"),  # Invalid credentials
     ("", "", "Your username is invalid!"),  # Blank fields
     (data["valid_user"], data["case_sensitive_password"], "Your password is invalid!"),  # Case sensitivity - password
     (data["special_character_username"], data["valid_password"], "Your username is invalid!"),  # Special char-username
     (data["valid_user"], data["special_character_password"], "Your password is invalid!"),  # Special char password
     (data["case_sensitive_user"], data["valid_password"], "Your username is invalid!")  # Case sensitivity - username
 ]


@pytest.mark.parametrize("username,password,expected", test_data)
def test_login_json_cases(driver, username, password, expected):
    # Step 1: Go on Login webpage
    driver.get("https://practice.expandtesting.com/login")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPage.login_button))

    # Step 2: Enter username and password
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LoginPage.username))
    driver.find_element(*LoginPage.username).clear()
    driver.find_element(*LoginPage.username).send_keys(username)
    driver.find_element(*LoginPage.password).clear()
    driver.find_element(*LoginPage.password).send_keys(password)

    # Step 3: Click Login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPage.login_button))
    driver.find_element(*LoginPage.login_button).click()

    # Step 4: Assertion
    if expected.startswith("Hi"):
        greeting = driver.find_element(*LoginPage.dashboard_welcome).text
        assert username.lower() in greeting.lower()
        # Logout only after valid login
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPage.logout_button))
        driver.find_element(*LoginPage.logout_button).click()
    else:
        error = driver.find_element(*LoginPage.error_message).text
        assert expected.lower() in error.lower()
