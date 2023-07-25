from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from config import config_data


class HeaderPage(GeneralHelpers):

    icon_lang = (By.XPATH, "//div[text()='English']")

    def open_url(self):
        self.driver.get(config_data['url'])

    def change_english(self):
        self.find_and_click(self.icon_lang)