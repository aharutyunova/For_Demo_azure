from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper


class Home(Helper):

    # locators
    btn_register_home = (By.XPATH, "//a[text()='Register']")
    btn_login_home = (By.XPATH, "//a[text()='Login']")
    btn_logout_home = (By.XPATH, "//a[text()='Logout']")



    
