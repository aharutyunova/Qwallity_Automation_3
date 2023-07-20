import time
from Helpers.driver_lib import Driver_Lib 
from Helpers.test_logger import logger
from Helpers.helpers import GeneralHelpers
from Pages import header
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Helpers import environment
from Pages.result import ResultPage
from Pages.favorite import Favorite
from Tests.search import Search
from Helpers.environment import config_data

"""

1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login

"""

def test_favorite_success_case(driver):
    helper = GeneralHelpers(driver)
    #headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    #test_helper = Search(driver)
    #loginpage = LoginPage(driver)
    favoritepage = Favorite(driver)

    helper.go_to_page(config_data["url"])
    helper.find_and_click(header.icon_lang)
    favorite_page = resultpage.add_to_favorites()
    logger("test_favorite_success_case() is passed!")



if __name__ == '__main__':
    driver = Driver_Lib().get_driver()
    test_favorite_success_case(driver)



