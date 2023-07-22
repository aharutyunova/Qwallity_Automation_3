from selenium import webdriver


class Driver_Lib:

    def get_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def quite_driver(self):
        self.driver.quit()
