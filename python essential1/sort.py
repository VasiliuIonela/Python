import time

from selenium.webdriver.common.by import By

from browser import Browser


class TestSortByName(Browser):
    URL = 'http://live.techpanda.org/index.php/'
    def navigate_to_site(self):
        self.browser.get(self.URL)

    def click_mobile(self):
        self.browser.find_element(By.XPATH, "//a[text()='Mobile']").click()

    def click_sort_by(self):
        self.browser.find_element(By.XPATH, "//select[@title='Sort By']").click()

    def sort_by_name(self):
        self.browser.find_element(By.XPATH,
                                  '//option[@value="http://live.techpanda.org/index.php/mobile.html?dir=asc&order=name"]').click()
