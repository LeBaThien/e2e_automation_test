from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def is_results_page_displayed(self):
        return "search" in self.driver.current_url
