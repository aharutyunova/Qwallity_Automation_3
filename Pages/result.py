from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from TestData import testdata

import random

result_container = (By.XPATH, "//div[@id='contentr']") #changed xpath //div[@id='contentr']//div[@class='dl']//a 
ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']") 
usd_price = (By.XPATH, "//div[text()='$ (USD)']")
from_price = (By.XPATH, "//input[@id='idprice1']")#corrected xpath
favorite_items = (By.XPATH, "//div[@id='contentr']//a")
to_price = (By.XPATH, "//input[@id='idprice2']")#corrected xpath
price_blue_button = (By.XPATH, "//a[@class='btn']//img[@id='gobtn']") #corrected xpath
contentr_items = (By.XPATH, "//div[@id='contentr']//div[@class='dl']//a")#corrected xpath
result_price = (By.XPATH, "//div[@id='contentr']//div[@class='p']")

# Good that you changes xpaths, again same note about to have locators outside or inside the class

class ResultPage(GeneralHelpers):

    def select_usd_currency(self):
        self.find_and_click(ddl_currency)
        self.find_and_click(usd_price)
        
    def set_price(self, price_min, price_max):
        self.find_and_send_keys(from_price,price_min)
        self.find_and_send_keys(to_price,price_max)
        self.find_and_click(price_blue_button)
    
    def check_result(self):
        self.find(contentr_items)#added new command firstly to get
        #div where will be the items in desirable range
        # self.driver.save_screenshot("screenshot.png")
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number   
       

    
   



