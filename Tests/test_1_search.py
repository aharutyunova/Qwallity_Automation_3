"""All necessary imports."""
from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers import environment
from Helpers.test_logger import logger
from TestData import testdata
from Tests.some_helpers import TESTHelpers


def test_search(driver):
    """Test case for search functionality."""
    result=TESTHelpers(driver)
    result.test_1_search(driver)
    




# Anna - this test case failed, because can't click on gobtn. Need to investigate and make it more stable

