from Helpers.driver_lib import Driver_Lib  
from Helpers import helpers
from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers.test_logger import logger
from TestData import testdata
from Helpers import environment
from Helpers.environment import config_data

"""
1. Navigate to lits.am
2. Search by "house" word
3. Filter by Currency with USD and Price with 0-50 $
4. Click on blue icon
5. Check that result's prices are in filtered range
"""    

def test_search_success_case(driver):
    helper = GeneralHelpers(driver)
    resultpage = ResultPage(driver)
    headerpage = HeaderPage(driver)

    helper.go_to_page(config_data["url"])
    headerpage.change_english()

        
    headerpage.saerch_data(testdata.search_data)
    resultpage.select_usd_currency()
    resultpage.set_price(testdata.price_min, testdata.price_max)
    price_list = resultpage.check_result()
        
    for price in price_list:
        assert 0 <= price <= testdata.price_max, logger("Result is incorrect", error=True)
        
    logger("test_search_success_case() is passed!")


if __name__ == '__main__':
    driver = Driver_Lib().get_driver()
    test_search_success_case(driver)








