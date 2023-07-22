from selenium import webdriver
import pytest
import logging

logging.basicConfig(filename='test_run.log',
                    filemode='a+', format='%(created)f - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
    yield logger
