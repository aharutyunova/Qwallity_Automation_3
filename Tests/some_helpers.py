from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Pages.result import ResultPage
from TestData import testdata


class TESTHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.general_helpers = GeneralHelpers(driver)
        self.header_page = HeaderPage(driver)
        self.login_page = LoginPage(driver)
        self.result_page = ResultPage(driver)
        self.price_list = None

    def test_1_search(self):
        self.general_helpers.go_to_page(environment.config_data["url"])
        self.header_page.change_english()
        self.header_page.saerch_data(testdata.search_data)
        self.header_page.select_usd_currency()
        self.result_page.set_price(testdata.price_min, testdata.price_max)
        self.price_list = self.result_page.check_result()

        for price in self.price_list:
            assert 0 <= price <= 50, "Result is incorrect"

        logger("Result is correct!")

    def change_to_and_click(self):
        self.header_page.change_english()
        self.header_page.click_myaccount()

    def login_page(self):
        self.login_page.login()

# Anna - you don't need this some_helpers file. You should keep page methods in pages, tests in test files
#  This some helpers file is additional

    def enter_logo_and_menu_tab(self):
        self.header_page.click_on_logo()
        self.header_page.click_menu_tab()
