from Helpers.test_logger import logger
from Pages.header import HeaderPage
from Pages.result import ResultPage
from TestData import test_data

"""
1. Navigate to lits.am
2. Search by "house" word
3. Filter by Currency with USD and Price with 0-50 $
4. Click on blue icon
5. Check that result's prices are in filtered range
"""


def test_search_item(driver):
    result_page = ResultPage(driver)
    header_page = HeaderPage(driver)
    result_page.go_to_page(test_data.url)
    header_page.change_english()
    header_page.search_data(test_data.search_word)
    result_page.select_usd_currency()
    result_page.set_price(test_data.price_min, test_data.price_max)
    driver.price_list = result_page.check_result()
    for price in driver.price_list:
        assert 0 <= price <= 50, \
            logger("Result of searching items is incorrect",
                   error=True)
    logger(f"Searching result is correct for the filtered prices")
