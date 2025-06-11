from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
from faker import Faker

faker_obj = Faker()


class Register(Helper):

    # locators
    inp_name = (By.XPATH, "//input[@id='name']")
    inp_email = (By.XPATH, "//input[@id='email']")
    inp_username = (By.XPATH, "//input[@id='username']")
    inp_pass = (By.XPATH, "//input[@id='password']")
    inp_confirm_pass = (By.XPATH, "//input[@id='confirm']")
    btn_submit = (By.XPATH, "//input[@value='Submit']")

    def register_user(self):
        user_name = faker_obj.user_name()
        password = faker_obj.pystr(min_chars=8, max_chars=8)

        self.find_and_send_keys(self.inp_name, faker_obj.name())
        self.find_and_send_keys(self.inp_email, faker_obj.email())
        self.find_and_send_keys(self.inp_username, user_name)
        self.find_and_send_keys(self.inp_pass, password)
        self.find_and_send_keys(self.inp_confirm_pass, password)
        self.find_and_click(self.btn_submit)
        return user_name, password
