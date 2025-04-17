import json
import os
import random
import string
from tests import file_path
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.register_page import RegisterPage


# Load JSON test data
with open(file_path) as file:
    data = json.load(file)


# Randomly generate new username
def get_name():
    name = string.ascii_lowercase
    new_user = (''.join(random.choice(name) for i in range(6)))
    return new_user


# Test cases derived from your Excel (manually defined)
register_data = [
    (get_name(), data["valid_new_password"], data["valid_new_password"], data["success_msg"]),
    (get_name(), data["valid_new_password"], data["confirm_password"], "Passwords do not match."),
    ("", "", "", "All fields are required."),
    (get_name(), "", "", "All fields are required."),
    ("us", data["valid_new_password"], data["valid_new_password"], "Username must be at least 3 characters long."),
    (data["long_user"], data["valid_new_password"], data["valid_new_password"], data["error_msg"])
]


@pytest.mark.parametrize("username, password, confirm_password, expected", register_data)
def test_register_functionality(driver, username, password, confirm_password, expected):
    # Step 1: Navigate to register page
    driver.get("https://practice.expandtesting.com/register")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RegisterPage.register_button))

    # Step 2: Fill form fields
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterPage.username))
    driver.find_element(*RegisterPage.username).clear()
    driver.find_element(*RegisterPage.username).send_keys(username)
    driver.find_element(*RegisterPage.password).clear()
    driver.find_element(*RegisterPage.password).send_keys(password)
    driver.find_element(*RegisterPage.confirm_password).clear()
    driver.find_element(*RegisterPage.confirm_password).send_keys(confirm_password)

    # Step 3: Submit the form
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPage.register_button))
    driver.find_element(*RegisterPage.register_button).click()

    # Step 4: Validate the result
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPage.message))
    result_text = driver.find_element(*RegisterPage.message).text

    assert expected.lower() in result_text.lower()
