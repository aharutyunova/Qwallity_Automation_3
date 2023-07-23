from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from testdata import test_data


class ResultPage(GeneralHelpers):

    inp_search = (By.ID, "idSearchBox")
    search_btn = (By.XPATH, "//button[@type='button']")
    from_price = (By.ID, "idprice1")
    to_price = (By.ID, "idprice2")
    ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
    usd_price = (By.XPATH, "//div[@data-name='$ (USD)']")
    price_blue_button = (By.ID, "gobtn")
    result_price = (By.XPATH, "//div[@class='p']")
   
    def search_data(self):
        self.find_and_send_keys(self.inp_search, test_data["search_data"])
        self.find_and_click(self.search_btn)
        
    def set_price_and_currency(self):
        self.find_and_send_keys(self.from_price, test_data["price_min"])
        self.find_and_send_keys(self.to_price, test_data["price_max"])
        self.find_and_click(self.price_blue_button)
        self.find_and_click(self.ddl_currency)
        self.find_and_click(self.usd_price)
          
    def get_result(self):
        elements = self.find_all(self.result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number      