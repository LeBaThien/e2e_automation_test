from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.BasePage import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")

    def search(self, keyword):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(keyword + Keys.RETURN)
