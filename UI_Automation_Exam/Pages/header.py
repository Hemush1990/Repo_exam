from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys

search_field = (By.XPATH, "//input[@id = 'idSearchBox']")
lang_icon = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, "//a[@href = '/category/4']")
logo = (By.ID, 'l')


class HeaderPage(GeneralHelpers):

    def search_data(self, search_word):
        self.find_and_send_keys(search_field, search_word)
        self.find(search_field).send_keys(Keys.ENTER)

    def change_english(self):
        self.find_and_click(lang_icon)

    def click_menu_tab(self):
        self.find_and_click(menu_tab)

    def click_on_logo(self):
        print('logo')
        self.find_and_click(logo)
