from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import allure
from page_objects.login_page import LoginPage  # here "login_page" is a file name and "LoginPage" is a class name
from allure_commons.types import AttachmentType


@allure.title("Nopcommerce Login Test")
@allure.description("TC#2 - nopcommerce App Positive Test")
@pytest.mark.positive
def test_nopcommerce_login_positive(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login_to_nopcommerce(usr="admin@yourstore.com", pwd="admin")
    print("Title", driver.title)
    time.sleep(5)
    assert driver.title == "Dashboard / nopCommerce administration"


@allure.title("Nopcommerce Logout Test")
@allure.description("TC#2 - nopcommerce App Positive Test")
@pytest.mark.positive
def test_logout(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.logout(usr="admin@yourstore.com", pwd="admin")
    print("Title", driver.title)
    time.sleep(5)
    assert driver.title == "Your store. Login"


# allure.attach(driver.get_screenshot_as_png(), name="login-Title", attachment_type=AttachmentType.PNG)

# parallel run :   pytest -n auto




