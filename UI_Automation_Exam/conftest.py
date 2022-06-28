import pytest
from selenium import webdriver

from Pages.header import HeaderPage
from Pages.login import LoginPage
from Pages.result import ResultPage
from TestData import test_data


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    header_page = HeaderPage(driver)
    result_page = ResultPage(driver)
    login_page = LoginPage(driver)

    result_page.go_to_page(test_data.url)
    header_page.change_english()
    login_page.click_myaccount()
    login_page.login()
