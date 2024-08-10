import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Login_Locator.LoginLocator import LoginLocator


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, name):
        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        username.send_keys(name)
        time.sleep(5)

    def enter_password(self, pass_word):
        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        password.send_keys(pass_word)
        time.sleep(5)

    def click_login(self):
        login = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginLocator.LOGIN_BUTTON))
        login.click()
        time.sleep(5)
