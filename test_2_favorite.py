import time

from Qwallity_Automation_3.Helpers.helpers import GeneralHelpers
from Qwallity_Automation_3.Pages import header
from Qwallity_Automation_3.Pages.header import HeaderPage
from Qwallity_Automation_3.Pages.login import LoginPage
from Qwallity_Automation_3.Helpers import environment
from Qwallity_Automation_3.Pages.result import ResultPage
from Qwallity_Automation_3.Pages.favorite import Favorite
from Qwallity_Automation_3.Tests.some_helpers import TESTHelpers
import time
"""

1. Navigate to list.am
2. Try add random item as favorite
3. System show popup for required login

"""

def test_favorite(driver):
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    time.sleep(10)
    resultpage = ResultPage(driver)
    test_helper = TESTHelpers(driver)
    loginpage = LoginPage(driver)
    time.sleep(10)
    favoritepage = Favorite(driver)
    time.sleep(10)


    helper.go_to_page("https://www.list.am/")
    helper.find_and_click(header.icon_lang)
    favorite_item = resultpage.add_to_favorites()



