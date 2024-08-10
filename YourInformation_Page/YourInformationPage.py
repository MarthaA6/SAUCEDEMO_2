import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from YourInformation_Locator.YourInformationLocator import YourInformationLocator


class YourInformationPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, martha):
        enter_first_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(YourInformationLocator.FIRST_NAME))
        enter_first_name.send_keys(martha)
        time.sleep(5)

    def enter_last_name(self, name):
        enter_last_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(YourInformationLocator.LAST_NAME))
        enter_last_name.send_keys(name)
        time.sleep(5)

    def enter_zip_postal_code(self, asdfg):
        enter_zip_postal_code = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(YourInformationLocator.ZIP_POSTAL_CODE))
        enter_zip_postal_code.send_keys(asdfg)
        time.sleep(5)

    def continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(YourInformationLocator.CONTINUE_BUTTON))
        continue_button.click()
        time.sleep(5)
