from selenium.webdriver.common.by import By


class LoginPage:
    # Login Locators
    login_webpage = (By.CSS_SELECTOR, "a[href='/login'][type='button']")
    username = (By.ID, "username")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.ID, "flash")
    dashboard_welcome = (By.ID, "username")
    logout_button = (By.XPATH, "//i[contains(@class, 'icon-signout')]/parent::a")
    dismiss_button = (By.ID, "dismiss-button")
