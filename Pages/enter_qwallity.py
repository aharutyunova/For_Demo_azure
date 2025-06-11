from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import config

class EntryQwallity(Helper):

    # locators
    entry_email = (By.XPATH, "//input[@id='email']")
    entry_code = (By.XPATH, "//input[@id='code']")
    btn_send = (By.XPATH, "//button[@id='Send']")
    btn_Login = (By.XPATH, "//a[text()= 'Login']")


    def enter_to_qwallity_app(self):
        self.find_and_send_keys(self.entry_email, config.security_email)
        self.find_and_send_keys(self.entry_code, config.security_code)
        self.find_and_click(self.btn_send)
        self.find_elem_ui(self.btn_Login)
