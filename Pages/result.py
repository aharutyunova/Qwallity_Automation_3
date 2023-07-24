from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import random


ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
usd_price = (By.XPATH, "//div[text()='$ (USD)']")
from_price = (By.ID, "idprice1")
to_price = (By.ID, "idprice2")
price_blue_button = (By.ID, "gobtn")
result_item = (By.XPATH, "//*[@id="tp"]/div[2]/a/div/div[1]") # Anna - quotes next to tp should be single, if you use double quotes for xpath. Locator also not effective
result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
login_require_popup = (By.XPATH, "//*[@id="main"]/div[1]/div[1]") # Anna the same comment for this locator


class ResultPage(GeneralHelpers):

    def select_usd_currency(self):
        self.find_and_click(ddl_currency)
        self.find_and_click(usd_price)
        
    def set_price(self, price_min, price_max):
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        self.find_and_click(price_blue_button)
    
    def check_result(self):
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number      

    def add_to_favorites(self):
        i =random.randint(0, 5)
        item = self.find(result_item)
        item.click()
        self.switch_to_window()
        self.wait_for_page('item')
        self.find_and_click(add_to_favorite)
        assert self.find(login_require_popup)
   
