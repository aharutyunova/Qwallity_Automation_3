"""Imports: selenium.webdriver.common.by, Helpers.helpers, time."""
from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import time

favorite_ads = (By.XPATH, "//div[text()='Favorite Ads']")
my_account_icon = (By.XPATH, '//*[@id="ma"]')

class Favorite(GeneralHelpers):
    """A class that represents the Favorite page and provides methods to interact with it."""
    
    favorite_items = (By.XPATH, "//div[@id='contentr']//a")
    favorite_items_remove = (By.XPATH, '//div[@original-title="Remove from favorites"]')

    def check_favorite_ads(self):
        """Check and clicks on the 'Favorite Ads' link after hovering over the 'My Account' icon."""
        self.hover_elem(self.find(my_account_icon))
        time.sleep(2)
        self.find_and_click(favorite_ads)

    def clear_favorites(self):
        """Clear the favorite items by clicking on the 'Remove from favorites' links."""
        f_items = self.find_all(self.favorite_items_remove)
        if f_items:
            for f_item in f_items:
                time.sleep(0.5)
                f_item.click()
