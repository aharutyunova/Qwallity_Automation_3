from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from werkzeug.debug.repr import helper

from Qwallity_Automation_3.Helpers import environment
from Qwallity_Automation_3.Helpers.helpers import GeneralHelpers
from Qwallity_Automation_3.Helpers.test_logger import logger
from selenium.webdriver.common.action_chains import ActionChains
from Qwallity_Automation_3.Pages.header import HeaderPage
from Qwallity_Automation_3.Pages.login import LoginPage
from Qwallity_Automation_3.Pages.result import ResultPage
from Qwallity_Automation_3.TestData import testdata

class TESTHelpers(ResultPage, LoginPage, HeaderPage):
    price_list = None

    def test_1_search(self, driver):
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
        self.change_english()
        self.click_myaccount()

    def login_page(self):
        self.login()

    def enter_logo_and_menu_tab(self):
        self.click_on_logo()
        self.click_menu_tab()