from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers import environment
from Helpers.test_logger import logger
from TestData import testdata
from some_helpers import TESTHelpers

"""
1. Navigate to lits.am
2. Search by "house" word
3. Filter by Currency with USD and Price with 0-50 $
4. Click on blue icon
5. Check that result's prices are in filtered range
"""


def test_search(driver):
    result=TESTHelpers(driver)
    result.test_1_search(driver)

# Get the price range from the testdata dictionary
    price_min = int(testdata.price_min)
    price_max = int(testdata.price_max)

    price_list = result.check_result()

    # Verify that all prices in the price list are within the expected range
    for price in price_list:
        assert price_min <= price <= price_max, f"Price '{price}' is within the expected range of {price_min}-{price_max}."

    logger("All result's prices are within the filtered range!")







# Anna -this test case is unstable, pass only with debug mode