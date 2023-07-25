from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import time
import random

favorite_ads = (By.XPATH, "//div[text()='Favorite Ads']")
my_account_icon = (By.XPATH, '//*[@id="ma"]')
login_require_popup = (By.XPATH, "//a[text()='Login to List.am']")
add_to_favorite = (By.XPATH, "//div[@id='sstar']//div")
result_item = (By.XPATH, "//div[@class='c c1']//a[1]")  #corrected xpath

class Favorite(GeneralHelpers):
    favorite_items = (By.XPATH, "//div[@id='contentr']//a")
    favorite_items_remove = (By.XPATH, '//div[@original-title="Remove from favorites"]')
    login_needed_msg = (By.XPATH, "//div[@id='dialog']//div[contains(@style,'margin')]")

    def check_favorite_ads(self):
        self.hover_elem(self.find(my_account_icon))
        time.sleep(2)
        self.find_and_click(favorite_ads)

    def add_to_favorites(self):
        #changed this function from result page to 
        #here as this is function for add item to favorite test case
        random_index =random.randint(0, 5) #the variable name "i" changed more readable one 
        item = self.find(result_item)
        item.click()
        self.switch_to_window()
        self.wait_for_page('item')
        self.find_and_click(add_to_favorite)
        assert self.find(login_require_popup), "Login required pop-up is not found" 
        #added assertion note once test case failed

        # Anna - changes are good, but will be better assert directly in test case not in the page's method

    def clear_favorites(self):
        f_items = self.find_all(self.favorite_items_remove)
        if f_items:
            for f_item in f_items:
                time.sleep(0.5)
                f_item.click()

    def get_notice_loginpopup(self):
        return self.find_elem_text(self.login_needed_msg)
