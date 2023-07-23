from Pages.header import HeaderPage
from Pages.result import ResultPage
from testdata import test_data
import logging
import time


def test_search(driver):
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    
    headerpage.open_url()
    time.sleep(2)
    headerpage.change_english()
    resultpage.search_data()
    resultpage.set_price_and_currency()
    prices_result = resultpage.get_result()
    for price_result in prices_result:
        assert test_data['price_min'] <= price_result <= test_data['price_max'], logging.error("Test is failed")
        logging.info("Test case is successfully passed")       