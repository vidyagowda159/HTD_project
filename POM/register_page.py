import re
from Library.excel_lib import ReadExcel
from Library.config import Config


class RegisterPage:
    """ consists of the automation script/ business logic of  Registration page of demo web shop"""
    read_xl = ReadExcel()
    reg_locators = read_xl.read_locators(Config.REG_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        locator = self.reg_locators["register_link"]
        self.driver.find_element(*locator).click()

    def select_female_radio_btn(self):
        locator_name, locator_value = self.reg_locators["female_radio_btn"]
        self.driver.find_element(locator_name, locator_value).click()

    def select_male_radio_btn(self):
        locator = self.reg_locators["male_radio_btn"]
        self.driver.find_element(*locator).click()

    def enter_firstname(self, f_name):
        locator = self.reg_locators["firstname_txt"]
        self.driver.find_element(*locator).send_keys(f_name)

    def enter_lastname(self, l_name):
        locator = self.reg_locators["lastname_txt"]
        self.driver.find_element(*locator).send_keys(l_name)

    def enter_email(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"

        locator = self.reg_locators["email_txt"]
        self.driver.find_element(*locator).send_keys(email)

    def enter_password(self, pwd):
        if isinstance(pwd, float):
            pwd = str(int(pwd))

        assert len(pwd) >= 6, "password should have atleast 6 characters"
        locator = self.reg_locators["password_txt"]
        self.driver.find_element(*locator).send_keys(pwd)
        return pwd

    def confirm_password(self, c_pwd, actual_pwd):
        if isinstance(c_pwd, float):
            c_pwd = str(int(c_pwd))

        locator = self.reg_locators["confirm_password_txt"]
        assert actual_pwd == c_pwd, "passwords are different"
        self.driver.find_element(*locator).send_keys(c_pwd)