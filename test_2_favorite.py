import time
import logging
from Helpers.helpers import GeneralHelpers
from Pages import header
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Helpers import environment
from Pages.result import ResultPage
from Pages.favorite import Favorite
from some_helpers import TESTHelpers
from Helpers.test_logger import logger
from TestData import testdata

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



