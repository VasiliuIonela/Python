import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    #definim constante(cu litere majuscule)
    USERNAME ="tomsmith"
    PASSWORD ="SuperSecretPassword!"
    WRONG_PASSWORD = "Altceva"
    WRONG_USERNAME = "madalina"
    #definim selectorii de care avem nevoie pentru crearea testelor, care vor fi constante
    USERNAME_SELECTOR = (By.ID, "username")
    PASSWORD_SELECTOR = (By.ID, "password")
    LOGIN_SELECTOR = (By.XPATH, "//button")
    ERROR_MESSAGE = (By.ID, 'flash')
    SUCCESS_MESSAGE = (By.ID, 'flash')
    LOGOUT_SELECTOR = (By.CSS_SELECTOR, "i[class='icon-2x icon-signout']")
    JS_ALERT_LOCATOR = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    JS_MESSAGE = (By.CSS_SELECTOR, "#result")
    #JS_MESSAGE =(By.ID, 'result')
    JS_CONIRFM= (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    JS_PROMPT = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    CONTEXT_SELECTOR = (By.ID, "hot-spot")


    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Edge()
        #self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #time.sleep(2)

    def tearDown(self) -> None:
        #time.sleep(1)
        self.driver.quit()

    # vom trimite un text random in campurile de user  si parola, il vom selecta si il vom sterge, apoi vom trimite user si parola corecte,
    # folosind libraria Keys

    def test_valid_after_invalid(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys('Maria')
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(Keys.CONTROL, 'a')
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys('12345')
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        time.sleep(2)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD, Keys.ENTER)
        time.sleep(3)
        #self.driver.find_element(*self.LOGIN_SELECTOR).click()

    def test_js_alert(self):
        #CSS_SELECTOR  "button[onclick='jsAlert()']"
        self.driver.find_element(*self.JS_ALERT_LOCATOR).click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        #facem un assert pe elem result comparandu-l cu textul
        #print(self.driver.find_element(*self.JS_MESSAGE).text)
        assert self.driver.find_element(*self.JS_MESSAGE).text == 'You successfully clicked an alert'

    def test_js_cancel(self):
        self.driver.find_element(*self.JS_CONIRFM).click()
        time.sleep(2)
        self.driver.switch_to.alert.dismiss()
        time.sleep(2)
        assert self.driver.find_element(*self.JS_MESSAGE).text == "You clicked: Cancel"

    def test_js_prompt(self):
        text = 'acesta este un mesaj de alerta'
        self.driver.find_element(*self.JS_PROMPT).click()
        time.sleep(2)
        self.driver.switch_to.alert.send_keys(text)
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)
        #assert self.driver.find_element(*self.JS_MESSAGE).text == 'You entered: acesta este un mesaj de alerta'
        #result =self.driver.find_element(*self.JS_MESSAGE).text
        self.assertEqual(self.driver.find_element(*self.JS_MESSAGE).text, f'You entered: {text}')
    def test_alert_from_context_menu(self):
        ac = ActionChains(self.driver)
        #construim selector pentru zona in care trebuie sa facem click drp
        element = self.driver.find_element(*self.CONTEXT_SELECTOR)
        ac.context_click(element).perform() # click dreapta
        time.sleep(3)
        self.driver.switch_to.alert.accept()
        time.sleep(3)








