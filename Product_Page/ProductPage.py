import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Product_Locator.ProductLocator import ProductLocator


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sauce_labs_backpack_1(self):
        click_sauce_labs_backpack_1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.SAUCE_LABS_BACKPACK_1))
        click_sauce_labs_backpack_1.click()
        time.sleep(5)

    def click_sauce_labs_bike_light_2(self):
        click_sauce_labs_bike_light_2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.SAUCE_LABS_BIKE_LIGHT_2))
        click_sauce_labs_bike_light_2.click()
        time.sleep(5)

    def click_sauce_labs_bolt_t_shirt_3(self):
        click_sauce_labs_bolt_t_shirt_3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.SAUCE_LABS_BOLT_T_SHIRT_3))
        click_sauce_labs_bolt_t_shirt_3.click()
        time.sleep(5)

    def click_sauce_labs_fleece_jacket_4(self):
        click_sauce_labs_fleece_jacket_4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.SAUCE_LABS_FLEECE_JACKET_4))
        click_sauce_labs_fleece_jacket_4.click()
        time.sleep(5)

    def click_sauce_labs_onesie_5(self):
        click_sauce_labs_onesie_5 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.SAUCE_LABS_ONESIE_5))
        click_sauce_labs_onesie_5.click()
        time.sleep(5)

    def click_test_all_the_things_t_shirt_6(self):
        click_test_all_the_things_t_shirt_6 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(ProductLocator.TEST_ALL_THE_THINGS_T_TSHIRT_6))
        click_test_all_the_things_t_shirt_6.click()
        time.sleep(5)
