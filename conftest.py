import pytest
from selenium import webdriver
import logging

logging.basicConfig(filename='test_run.log', 
                    format='%(filename)s - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()