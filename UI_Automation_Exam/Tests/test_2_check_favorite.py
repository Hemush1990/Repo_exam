from Helpers.test_logger import logger
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Pages.favorite import Favorite

"""

1. Login to the system
2. Go to Electronics page
3. Add random number of products as a favorite
4. Go to My Account-> Favorite Ads
5. Check that Favorite page contains correct(selected) products

"""


def test_favorite_items(driver, login):
    header_page = HeaderPage(driver)
    result_page = ResultPage(driver)
    favorite_page = Favorite(driver)

    header_page.click_on_logo()
    favorite_page.check_favorite_ads()
    favorite_page.clear_favorites()
    header_page.click_on_logo()
    header_page.click_menu_tab()
    favorite_item_list = result_page.add_to_favorites()
    favorite_page.check_favorite_ads()
    my_favorite_list = favorite_page.get_favorite_items()
    header_page.click_menu_tab()
    favorite_page.check_favorite_ads()
    assert sorted(favorite_item_list) == sorted(my_favorite_list),\
        logger("Result of favorites is incorrect", error=True)
    logger("The favorite activity is correct ")
