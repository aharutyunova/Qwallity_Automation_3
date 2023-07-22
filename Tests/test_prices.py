from Page.main_page import Main_Page
from Page.search_page import Search_Page
from Data.test_data import test_data
from Lib.custom_logger import logger


def test(driver):
    main_page = Main_Page(driver)
    result_page = Search_Page(driver)

    main_page.open_page()
    main_page.choose_language()
    prices = result_page.get_prices()

    for price in prices:
        splited = ((price.text).split(" "))[0].split("$")
        number = int(splited[1])
        assert int(test_data["price_from"]) <= number <= int(
            test_data["price_to"]), logger("Fail", True)
    logger("Test is passed!! The prices are in selected range.")
