import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Shopping_Cart_Locator.ShoppingCartLocator import ShoppingCartLocator


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def shopping_cart_button(self):
        shopping_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ShoppingCartLocator.SHOPPING_CART_BUTTON))
        shopping_cart_button.click()
        time.sleep(5)
