import pytest
from selenium import webdriver
import logging

logging.basicConfig(filename='test_run.txt',
                    filemode='a+',
                    format='%(created)f - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)

    yield logging.getLogger()
