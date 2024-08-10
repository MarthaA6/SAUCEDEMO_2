import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Collapsible_Locator.CollapsibleLocator import CollapsibleLocator


class CollapsiblePage:
    def __init__(self, driver):
        self.driver = driver

    def collapsible_button(self):
        collapsible_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CollapsibleLocator. COLLAPSIBLE_BUTTON))
        collapsible_button.click()
        time.sleep(5)
