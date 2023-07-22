import time
from Helpers.driver_lib import Driver_Lib
from Helpers.helpers import GeneralHelpers
from Helpers.test_logger import logger
from Pages import header
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Pages.result import ResultPage
from Pages.favorite import Favorite
from Helpers import environment
from Helpers.environment import config_data


def test_favorite_success_case(driver):
    helper = GeneralHelpers(driver)
    resultpage = ResultPage(driver)

    helper.go_to_page(config_data["url"])
    helper.find_and_click(header.icon_lang)
    resultpage.add_to_favorites()

    logger("test_favorite_success_case() is passed!")
