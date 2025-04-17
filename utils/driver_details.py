import json
from tests import file_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# read data from json file
with open(file_path) as data_file:
    # dt=data_file.read()
    data = json.load(data_file)


class Driver:
    @staticmethod
    def get_driver():
        # ✅ Create Chrome options
        chrome_options = Options()

        # ✅ Disable password manager and update prompts
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "safebrowsing.enabled": False,
            "safebrowsing.disable_download_protection": True,
            "profile.default_content_setting_values.notifications": 2
        }
        chrome_options.add_experimental_option("prefs", prefs)

        # Disable password bubble AND safe browsing prompts
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-features=PasswordLeakDetection,SafeBrowsingEnhancedProtection")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--incognito")

        service = Service(executable_path=data["chrome_driver_path"])
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
