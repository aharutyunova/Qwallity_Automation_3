from Lib.general_lib import General_Helper
from selenium.webdriver.common.by import By
from Data.config import config_data


class Main_Page(General_Helper):
    welcome_form = (By.XPATH, "//div[@id='dlgLangSel']")
    english = (By.XPATH, "//div[text()='English']")

    def open_page(self):
        self.driver.get(config_data["url"])

    def choose_language(self):
        self.find_and_click(self.english)
