from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData import testdata
import time

inp_search = (By.ID, "idSearchBox")
icon_lang = (By.XPATH, "//div[text()='English']")


class HeaderPage(GeneralHelpers):

    def search_data(self, test_data):
        self.find_and_send_keys(inp_search, test_data)
        self.find(inp_search).send_keys(Keys.ENTER)

    def change_english(self):
        self.find_and_click(icon_lang)
