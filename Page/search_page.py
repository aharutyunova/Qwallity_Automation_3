from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from Data.test_data import test_data
from selenium.webdriver.common.keys import Keys


class Search_Page(General_Helper):
    search_field = (By.ID, "idSearchBox")
    currency = (
        By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
    usd = (
        By.XPATH, "//div[@data-name='$ (USD)']")
    price_from = (By.XPATH, "//input[@id='idprice1']")
    price_to = (By.XPATH, "//input[@id='idprice2']")
    go_btn = (By.ID, "gobtn")
    prices = (By.XPATH, "//div[@class='p']")

    def get_prices(self):
        self.find_and_send_keys(self.search_field, test_data["text"])
        self.find(self.search_field).send_keys(Keys.ENTER)
        self.find_and_send_keys(self.price_from, test_data["price_from"])
        self.find_and_send_keys(self.price_to, test_data["price_to"])
        self.find_and_click(self.go_btn)
        self.find_and_click(self.currency)
        self.find_and_click(self.usd)
        prices = self.find_elements(self.prices)
        return prices
