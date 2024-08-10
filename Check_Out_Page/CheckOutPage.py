import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Check_Out_Locator.CheckOutLocator import CheckOutLocator


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    def continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckOutLocator.CONTINUE_BUTTON))
        continue_button.click()
        time.sleep(5)
