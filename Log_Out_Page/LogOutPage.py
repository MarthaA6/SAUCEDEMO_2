import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Log_Out_Locator.LogOutLocator import LogOutLocator


class LogOutPage:
    def __init__(self, driver):
        self.driver = driver

    def log_out_button(self):
        log_out_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LogOutLocator.LOG_OUT_BUTTON))
        log_out_button.click()
        time.sleep(5)
