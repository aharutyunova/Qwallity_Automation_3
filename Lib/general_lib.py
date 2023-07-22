from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Lib.custom_logger import logger


class General_Helper():

    def __init__(self, driver):
        self.driver = driver

    def find(self, loc, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout=timeout).until(
                EC.visibility_of_element_located(loc))
            return elem
        except Exception as e:
            logger(f"Element not found", True)

    def find_elements(self, loc, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout=timeout).until(
                EC.visibility_of_all_elements_located(loc))
            return elem
        except Exception as e:
            logger(f"Element not found", True)

    def find_and_click(self, loc, timeout=60):
        elem = self.find(loc)
        try:
            elem.click()
            logger(f"Element is clickable")
        except Exception as e:
            logger("Could not click on element", True)

    def find_and_send_keys(self, loc, text, timeout=60):
        elem = self.find(loc, timeout=timeout)
        try:
            elem.send_keys(text)
        except Exception as e:
            logger(f"Could not input {text} in the field", True)

    def find_text(self, loc, timeout=60):
        elem = self.find(loc, timeout=timeout)
        return elem.text

    def get_element_value(self, loc, timeout=60, attempts=3):
        elem = self.find(loc, timeout=timeout)
        while attempts:
            value = elem.get_attribute('value')
            if value:
                return value
            time.sleep(0.3)
            attempts -= 1
