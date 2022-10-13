class Config:

    URL = "https://demowebshop.tricentis.com/"
    CHROME_PATH = r"../drivers/chromedriver.exe"
    FIREFOX_PATH = r"../drivers/geckodriver.exe"
    MSEDGE_PATH = r"../drivers/msedgedriver.exe"

    TESTDATA_PATH = r"../test_data/demowebshop_testdata.xlsx"
    LOCATORS_PATH = r"../test_data/locators.xlsx"

    REG_TESTDATA_SHEET = "reg_credentials"
    REG_LOCATORS_SHEET = "reg_objects"

    LOGIN_LOCATORS_SHEET = "login_objects"
    LOGIN_TESTDATA_SHEET = "login_credentials"

    REPORTS_PATH = r"../reports/"
    SCREENSHOT_PATH = r"../screenshots/"
