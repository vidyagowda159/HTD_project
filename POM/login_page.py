from Library.excel_lib import ReadExcel
from Library.config import Config


class LoginPage:
    """ consists of the automation script/ business logic of Login page of demo web shop"""
    read_xl = ReadExcel()
    login_locators = read_xl.read_locators(Config.LOGIN_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        locator = self.login_locators["login_link"]
        self.driver.find_element(*locator).click()

    def enter_email(self, email):
        locator = self.login_locators["email_txt"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_password(self, pwd):
        locator = self.login_locators["pwd_txt"]
        self.driver.find_element(*locator).send_keys(pwd)

    def click_remember_me_checkbox(self):
        locator = self.login_locators["remember_check_box"]
        self.driver.find_element().click()

    def click_forgot_pwd(self):
        locator = self.login_locators["forgot_pwd"]
        self.driver.find_element().click()

    def click_login_btn(self):
        locator = self.login_locators["login_btn"]
        self.driver.find_element().click()


