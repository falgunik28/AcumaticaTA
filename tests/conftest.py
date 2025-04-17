import pytest

from utils.driver_details import Driver


@pytest.fixture(scope="module")
def driver():
    driver = Driver.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
