from Pages.favorite import Favorite
from Pages.header import HeaderPage
from testdata import test_data
import logging
import time


def test_favorite(driver):
    headerpage = HeaderPage(driver)
    favoritepage = Favorite(driver)

    headerpage.open_url()
    time.sleep(2)
    headerpage.change_english()
    popuptxt = favoritepage.add_to_favorites()
    popup_txt_check = popuptxt.text
    assert test_data['popuptxt'] == popup_txt_check, logging.error("Test is failed")
    logging.info("Test case is successfully passed")