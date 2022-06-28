from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from Helpers.test_logger import logger
import random
import time

ddl_currency = (By.XPATH, "//*[@id = '_idcrc']//following::div[@class='me']")
usd_price = (By.XPATH, "//div[text()='$ (USD)']")
from_price = (By.ID, "idprice1")
result_items = (By.XPATH, "//div[@id='contentr']//a")
to_price = (By.ID, "idprice2")
price_blue_button = (By.ID, "gobtn")
result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
add_to_favorite = (By.ID, "sstar")


class ResultPage(GeneralHelpers):

    def select_usd_currency(self):
        self.find_and_click(ddl_currency)
        self.find_and_click(usd_price)
        logger("USD currency is set")

    def set_price(self, price_min, price_max):
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        self.find_and_click(price_blue_button)
        logger(f"Prices from {price_min} to {price_max} are set")

    def check_result(self):
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0])
                             for el in price_list]
        logger(f"Prices list is {price_list_number}")
        return price_list_number

    def add_to_favorites(self):
        n = random.randint(0, 5)
        favorite_items_list = []
        items = self.find_all(result_items)
        for i in range(1, n+1):
            time.sleep(1)
            items[i].click()
            self.wait_for_page('item')
            self.find_and_click(add_to_favorite)
            item_from_url = self.return_url().split("/")[-1]
            favorite_items_list.append(item_from_url)
            logger(f"The item was added to favorite with id {item_from_url}")
            self.driver.back()
        return favorite_items_list
