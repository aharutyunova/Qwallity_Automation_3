"""Imports: selenium.webdriver.common.by, Helpers.helpers, selenium.webdriver.common.keys, TestData.testdata."""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
from selenium.webdriver.common.keys import Keys
from TestData import testdata

lbl_account = (By.XPATH, "//*[@id='ma']")
inp_search = (By.ID, "idSearchBox")
icon_lang = (By.XPATH, "//div[text()='English']")
menu_tab = (By.XPATH, f"//*[@id='menu']//a[text()='{testdata.menu_tab}']")
logo = (By.XPATH, '//*[@id="l"]')

class HeaderPage(GeneralHelpers):
    """Subclass of GeneralHelpers for header page actions."""
    
    def saerch_data(self, test_data):
        """Search for the provided test data in the search input and presses ENTER."""
        self.find_and_send_keys(inp_search, test_data)
        self.find(inp_search).send_keys(Keys.ENTER)
    def change_english(self):
        """Clicks on the language icon to change the language to English."""
        self.find_and_click(icon_lang)
    def click_menu_tab(self):
        """Clicks on the menu tab specified in the test data."""
        self.find_and_click(menu_tab)
    def click_on_logo(self):
        """Print 'logo' and clicks on the logo element."""
        print('logo')
        self.find_and_click(logo)

