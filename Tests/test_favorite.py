from Page.main_page import Main_Page
from Page.favorite_page import Favorite_Page
from Data.test_data import test_data
from Lib.custom_logger import logger


def test(driver):
    main_page = Main_Page(driver)
    favorite_page = Favorite_Page(driver)

    main_page.open_page()
    main_page.choose_language()
    login_form = favorite_page.get_login_form()
    assert login_form, logger("Test is failed.", True)
    logger("Test is passed!! The pop-up is opened")
