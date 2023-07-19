import pytest
from selenium import webdriver
import logging

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
