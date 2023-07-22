from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from Data.config import config_data


class Favorite_Page(General_Helper):
    item = (By.XPATH, "//*[@id='hcontent']/div/div/div[3]/div/a[1]/img")
    fav_btn = (
        By.XPATH, "//div[@id='sstar']/div[contains(@onclick,'Favorites')]")
    please_login_form = (By.XPATH, "//div[@id='dialog']")

    def get_login_form(self):
        self.find_and_click(self.item)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_and_click(self.fav_btn)
        login_form = self.find(self.please_login_form)
        return login_form
