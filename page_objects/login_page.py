# Page Class
# Page Locators
# Page Actions
# WebDriver Init
# Custom Functions
# No assertions (in Page Object Class)


# Login Page responsibility
# get username and send keys - email
# # get password and send keys - email
# # click the submit button and navigate to dashboard Page
# Invalid -> error message
# Forgot password


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from allure_commons.types import AttachmentType


class LoginPage:
    # Page Locator
    username = (By.NAME, "Email")
    password = (By.NAME, "Password")
    submit_button = (By.XPATH, "//button[normalize-space()='Log in']")
    logout_button = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    # Page Action

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_logout_button(self):
        return self.driver.find_element(*LoginPage.logout_button)

    # Main Page Action

    def login_to_nopcommerce(self, usr, pwd):
        self.get_username().clear()
        self.get_username().send_keys(usr)
        self.get_password().clear()
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def logout(self, usr, pwd):
        self.get_username().clear()
        self.get_username().send_keys(usr)
        self.get_password().clear()
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()
        self.get_logout_button().click()

