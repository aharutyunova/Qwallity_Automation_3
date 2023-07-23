import time
import logging
from Qwallity_Automation_3.Helpers.helpers import GeneralHelpers
from Qwallity_Automation_3.Pages import header
from Qwallity_Automation_3.Pages.header import HeaderPage
from Qwallity_Automation_3.Pages.login import LoginPage
from Qwallity_Automation_3.Helpers import environment
from Qwallity_Automation_3.Pages.result import ResultPage
from Qwallity_Automation_3.Pages.favorite import Favorite
from Qwallity_Automation_3.some_helpers import TESTHelpers
from Qwallity_Automation_3.Helpers.test_logger import logger
from Qwallity_Automation_3.TestData import testdata

"""

1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login

"""

def test_favorite(driver):
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    test_helper = TESTHelpers(driver)
    loginpage = LoginPage(driver)
    favoritepage = Favorite(driver)
    helper.go_to_page("https://www.list.am/")
    helper.find_and_click(header.icon_lang)
    favorite_item = favoritepage.add_to_favorites()
    assert favoritepage.get_notice_loginpopup() == testdata.note
    logger ("Test case is successfully passed!")



