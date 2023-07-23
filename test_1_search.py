from Qwallity_Automation_3.Helpers.helpers import GeneralHelpers
from Qwallity_Automation_3.Pages.header import HeaderPage
from Qwallity_Automation_3.Pages.result import ResultPage
from Qwallity_Automation_3.Helpers import environment
from Qwallity_Automation_3.Helpers.test_logger import logger
from Qwallity_Automation_3.TestData import testdata
from Qwallity_Automation_3.some_helpers import TESTHelpers

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






