from selenium import webdriver
class Browser:
    browser = webdriver.Firefox()
    browser.maximize_window()
    def close(self):
        self.browser.quit()