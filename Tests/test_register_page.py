import datetime
import pytest
from Library.excel_lib import ReadExcel
from POM.register_page import RegisterPage
from Library.config import Config


class TestRegisterPage:
    """ contains the test scripts for the above automation scripts"""

    read_xl = ReadExcel()
    data = read_xl.read_testdata(Config.REG_TESTDATA_SHEET)

    @pytest.mark.parametrize("f_name, l_name, email, pwd, c_pwd", data)
    def test_registration(self, f_name, l_name, email, pwd, c_pwd, init_driver):
        driver = init_driver
        try:
            rp = RegisterPage(driver)  # rp = RegisterPage(init_driver)
            rp.click_register_link()
            rp.select_male_radio_btn()
            rp.enter_firstname(f_name)
            rp.enter_lastname(l_name)
            rp.enter_email(email)
            actual_pwd = rp.enter_password(pwd)
            rp.confirm_password(c_pwd, actual_pwd)

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH + name)
            raise error_msg
