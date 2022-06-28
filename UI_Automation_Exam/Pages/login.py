from selenium.webdriver.common.by import By
from Helpers.test_logger import logger
from Helpers.helpers import GeneralHelpers
from TestData.environment import config_data_user_1

email_field = (By.ID, "_idyour_email")
pass_field = (By.ID, "_idpassword")
login_btn = (By.ID, "action__form_action0")
account_lbl = (By.XPATH, "//*[@id='ma']")


class LoginPage(GeneralHelpers):

    def login(self):
        self.find_and_send_keys(email_field, config_data_user_1["email"])
        self.find_and_send_keys(pass_field, config_data_user_1["password"])
        self.find_and_click(login_btn)
        self.wait_for_page('my')
        logger(f"The user has successfully logged to the system.")

    def click_myaccount(self):
        self.find_and_click(account_lbl)
        self.wait_for_page('login')
