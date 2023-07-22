"""Imports: time, Helpers.helpers, Pages.header, Pages.login, Helpers.environment, Pages.result, Pages.favorite, Tests.some_helpers."""
from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Helpers.environment import config_data
from Pages.result import ResultPage
from Pages.favorite import Favorite
from Tests.some_helpers import TESTHelpers

def test_favorite(driver):
    """Test case to navigate to list.am, add a random item as favorite, and check for the login popup."""
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    test_helper = TESTHelpers(driver)
    loginpage = LoginPage(driver)
    favoritepage = Favorite(driver)

    helper.go_to_page(config_data["url"])
    headerpage.change_english()
    favorite_item = resultpage.add_to_favorites()
