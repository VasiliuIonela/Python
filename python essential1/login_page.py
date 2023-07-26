import time
import unittest
from browser import Browser
from selenium.webdriver.common.by import By


class TestLogin(Browser):
    USERID = "mngr517505"
    PASSWORD = "vYhudYd"
    USERID_SELECTOR = (By.ID, "message23")
    PASSWORD_SELECTOR = (By.XPATH, "//input[@name='password']")
    LOGIN_SELECTOR = (By.XPATH, "//input[@value='LOGIN']")
    URL = 'https://www.demo.guru99.com/V4/'

    def navigate_to_login(self):
        time.sleep(3)
        self.browser.get(self.URL)

    def click_content(self):
        self.browser.find_element(By.XPATH, "//span[text()='Accept All']").click()

    def enter_userid(self):
        self.browser.find_element(*self.USERID_SELECTOR).send_keys(self.USERID)

    def enter_password(self):
        self.browser.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)

    def login_button(self):
        self.browser.find_element(*self.LOGIN_SELECTOR).click()

    def valid_login(self):
        assert "Welcome To Manager's Page" in self.browser.find_element(By.XPATH, "//marquee[@class='heading3']").text
