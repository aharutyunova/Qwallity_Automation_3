"""all nessary imports."""
import pytest
from selenium import webdriver
import logging

logging.basicConfig(filename='TestResults/test_run.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    """Pytest fixture providing a Chrome WebDriver instance."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def logger():
    """Provide a pytest fixture for logging messages with optional error logging."""
    def log_message(msg, error=False):
        if error:
            logging.error(msg)
        else:
            logging.info(msg)

    return log_message

