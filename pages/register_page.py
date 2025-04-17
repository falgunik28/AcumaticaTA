from selenium.webdriver.common.by import By


class RegisterPage:
    # Register Locators
    register_webpage = (By.CSS_SELECTOR, "a[href='/register'][type='button']")
    username = (By.ID, "username")
    password = (By.ID, "password")
    confirm_password = (By.ID, "confirmPassword")
    register_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    message = (By.ID,"flash")
