from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from Helpers.test_logger import logger

import time

favorite_ads_field = (By.XPATH, "//a[@href='/saved']")
account_lbl = (By.XPATH, "//div[@id = 'ma']//span")
result_items = (By.XPATH, "//div[@id='contentr']//a")
avatar_icon = (By.XPATH, "//div[@href = '/my']//img")
empty_favorites = (By.XPATH, "//img[@src = '/img/empty_heart.png']")


class Favorite(GeneralHelpers):
    favorite_items_remove = (By.XPATH, "//*[@class='star']")

    def check_favorite_ads(self):
        self.find(avatar_icon, should_exist=True)
        self.hover_elem(self.find(account_lbl))
        time.sleep(2)
        self.find_and_click(favorite_ads_field)

    def clear_favorites(self):
        f_items = self.find_all(self.favorite_items_remove)
        if f_items:
            for f_item in f_items:
                self.scroll_to_elem(f_item)
                f_item.click()
        elif empty_favorites:
            logger("There weren't any old items")
            self.driver.back()
        logger("All favorite items were deleted")

    def get_favorite_items(self):
        favorites = self.find_all(result_items)
        favorite_list = []
        for favorite in favorites:
            favorite.click()
            self.wait_for_page('item')
            item_from_url = self.return_url().split("/")[-1]
            favorite_list.append(item_from_url)
            self.driver.back()
        return favorite_list
