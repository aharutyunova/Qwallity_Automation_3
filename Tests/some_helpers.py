"""Imports: WebDriverWait, environment, logger, ActionChains, HeaderPage, ResultPage, testdata."""
from selenium.webdriver.support.wait import WebDriverWait
from Helpers import environment
from Helpers.test_logger import logger
from selenium.webdriver.common.action_chains import ActionChains
from Pages.header import HeaderPage
from Pages.result import ResultPage
from TestData import testdata

class TESTHelpers(ResultPage, HeaderPage):
    """TESTHelpers class: Inherits from ResultPage and HeaderPage classes.""" 
     
    price_list = None

    def test_1_search(self, driver):
        """Performs a search test with the given driver instance."""
        resultpage = ResultPage(driver)
        headerpage = HeaderPage(driver)
        self.go_to_page(environment.config_data["url"])
        self.change_english()
        headerpage.saerch_data(testdata.search_data)
        self.select_usd_currency()
        resultpage.set_price(testdata.price_min, testdata.price_max)
        self.price_list = resultpage.check_result()
        for price in self.price_list:
            assert 0 <= price <= 50, logger("Result is incorrect", error=True)
        logger("Result is correct!")

        return self

    def change_to_and_click(self):
        """Change the language to English and clicks on 'My Account'."""
        self.change_english()
        self.click_myaccount()

    def login_page(self):
        """Navigate to the login page."""
        self.login()

    def enter_logo_and_menu_tab(self):
        """Click on the logo and the menu tab."""
        self.click_on_logo()
        self.click_menu_tab()

# Anna  - you don't need this file, all methods should be or in libs, or in pages, test functions should be inside test files
# So methods of this file should be distributed by pages and tests