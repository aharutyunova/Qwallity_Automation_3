from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import logging


class GeneralHelpers:
    
    def __init__(self, driver):
        self.driver = driver

    def find_and_click(self, loc, timeout=30):
        elem = self.find(loc)
        try:
            elem.click()
            logging.info("Element is clickable")
        except Exception as e:
            logging.error("Could not click on element")

    def find_and_send_keys(self, loc, text, timeout=60):
        elem = self.find(loc, timeout=timeout)
        try:
            elem.send_keys(text)
        except Exception as e:
            logging.error(f"Could not input any number in the field")
    
    def find(self, loc, timeout=60):
        try:
            elem = WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(loc))
            return elem
        except Exception as e:
            logging.error(f"Element not found")

    def find_all(self, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(loc))
            return elements
        except Exception as e:
            logging.info(f"Found: {len(elements)}")

    def switch_to_window(self, i=1):
        self.driver.switch_to.window(self.driver.window_handles[i])

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])