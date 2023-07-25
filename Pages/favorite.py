from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import time


class Favorite(GeneralHelpers):
    
    first_item = (By.XPATH, "//*[@id='hcontent']/div/div/div[3]/div/a[1]/img")
    heart_icon = (By.XPATH, "//div[@class='off']")
    login_require_popup = (By.XPATH, "//div[contains (text(), 'Please')]")

    def add_to_favorites(self):
        self.find_and_click(self.first_item)
        time.sleep(2)
        self.switch_to_window()
        time.sleep(2)
        self.find_and_click(self.heart_icon)
        popuptext = self.find(self.login_require_popup)
        return popuptext  # Anna - very good you remove assertion from this method