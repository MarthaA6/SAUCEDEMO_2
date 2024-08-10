import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Overview_Locator.OverviewLocator import OverviewLocator


class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def finish_button(self):
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OverviewLocator.FINISH_BUTTON))
        finish_button.click()
        time.sleep(5)
