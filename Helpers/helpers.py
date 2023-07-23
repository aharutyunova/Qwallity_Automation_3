from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from Helpers.test_logger import logger


class GeneralHelpers:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_page(self, url):
        logger(f"Navigate to {url}")
        self.driver.get(url)
        self.driver.maximize_window()

    def switch_to_window(self, window_index=1):
        if window_index < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            self.driver.maximize_window()
        else:
            raise IndexError("Window index out of range.")

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def find_and_click(self, locator, timeout=60):
        element = self.find(locator, timeout)
        logger(f"Click on {locator[1]}")
        element.click()

    def find_and_send_keys(self, locator, input_text, timeout=60):
        element = self.find(locator, timeout)
        logger(f"Send '{input_text}' to {locator[1]}")
        element.send_keys(input_text)

    def find(self, locator, timeout=20, should_exist=True, get_text="", get_attribute=""):
        logger(f"Search element '{locator[1]}'")
        try:
            elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator),
                message=f"Element '{locator}' not found!"
            )

            if get_text:
                logger(f"Element text: {elem.text}")
                return elem.text
            elif get_attribute:
                return elem.get_attribute(get_attribute)
            else:
                return elem
        except Exception as e:
            logger(f"Error occurred: {e}")
            raise

    def find_all(self, locator, timeout=10):
        logger(f"Search elements '{locator[1]}'")
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator),
                message=f"Elements '{locator}' not found!"
            )
            logger(f"Found: {len(elements)}")
            return elements
        except Exception as e:
            logger(f"Error occurred: {e}")
            raise

    def wait_for_page(self, page="", not_page="", timeout=10):
        try:
            if page:
                WebDriverWait(self.driver, timeout).until(EC.url_contains(page))
            elif not_page:
                WebDriverWait(self.driver, timeout).until_not(EC.url_contains(not_page))
        except Exception as e:
            logger(f"Error occurred: {e}")
            raise

    def retrn_url(self):
        return str(self.driver.current_url)

    def hover_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def close_driver(self):
        self.driver.quit()

