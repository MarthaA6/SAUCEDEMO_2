import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Check_Out_Page.CheckOutPage import CheckOutPage
from Collapsible_Page.CollapsiblePage import CollapsiblePage
from Config.Config import ConfigYourInfo, ConfigLogin
from Log_Out_Page.LogOutPage import LogOutPage
from Login_Page.LoginPage import LoginPage
from Overview_Page.OverviewPage import OverviewPage
from Product_Page.ProductPage import ProductPage
from Shopping_Cart_Page.ShoppingCartPage import ShoppingCartPage
from YourInformation_Page.YourInformationPage import YourInformationPage


@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    # Uncomment the line below to run in headless mode
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url(ConfigLogin.BaseUrl)
    return login_page


def test_login_page_automation_playground(login):
    login.enter_username(ConfigLogin.USERNAME)
    login.enter_password(ConfigLogin.PASSWORD)
    login.click_login()


def test_product_page_on_sauce_demo(login):
    product_page = ProductPage(login.driver)
    product_page.click_sauce_labs_backpack_1()
    product_page.click_sauce_labs_bike_light_2()
    product_page.click_sauce_labs_bolt_t_shirt_3()
    product_page.click_sauce_labs_fleece_jacket_4()
    product_page.click_sauce_labs_onesie_5()
    product_page.click_test_all_the_things_t_shirt_6()


def test_shopping_cart_on_automation_playground(login):
    shopping_cart_button = ShoppingCartPage(login.driver)
    shopping_cart_button.shopping_cart_button()


def test_check_out_page_on_automation_playground(login):
    check_out_page = CheckOutPage(login.driver)
    check_out_page.continue_button()


def test_information_form_on_automation_playground(login):
    information_form = YourInformationPage(login.driver)
    information_form.enter_first_name(ConfigYourInfo.FIRST_NAME)
    information_form.enter_last_name(ConfigYourInfo.LAST_NAME)
    information_form.enter_zip_postal_code(ConfigYourInfo.ZIP_POSTAL)
    information_form.continue_button()


def test_overview_page_on_automation_playground(login):
    overview_page = OverviewPage(login.driver)
    overview_page.finish_button()


def test_collapsible_button_on_automation_playground(login):
    collapsible_button = CollapsiblePage(login.driver)
    collapsible_button.collapsible_button()


def test_log_out_button_on_automation_playground(login):
    test_log_out_button = LogOutPage(login.driver)
    test_log_out_button.log_out_button()
