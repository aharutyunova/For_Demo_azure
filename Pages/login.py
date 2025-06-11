from Helpers.general_helpers import Helper
from selenium.webdriver.common.by import By


class Login(Helper):

    # locators
    inp_username = (By.XPATH, "//input[@name='username']")
    inp_password = (By.XPATH, "//input[@name='password']")
    btn_login = (By.XPATH, "//button[@id='submit_login_page']")
    
    def login(self, username, password):
        try:
            self.find_and_send_keys(self.inp_username, username)
            self.find_and_send_keys(self.inp_password, password)
            self.find_and_click(self.btn_login)
        except Exception as e:
            print(e)