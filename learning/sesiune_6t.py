#unit test library
#   -creare de teste rulabile direct in interiorul clasei
#   -initial construita pt teste unitare
#   -pt a ne folosi de libraria unit test, trb sa cream o clasa de teste care sa mosteneasca clasa TestCase din libraria unittest
#  ex:  class TestAlerts(unittest.TestCase):
'''
metode obligatorii:
    setUp()
        -ne asiguram ca functioneza corescpunzator sistemul
        -toate activitatile care trebuie sa fie executate inainte de orice test din clasa respectiva
    tearDown()
        -eliberare sistemul de resurse
        -toate activitatile care trebuie sa fie executate dupa orice test din clasa respectiva
    toate metodele de test trebuie sa aiba prefixul: test_
    creare metode de test si executare metode
    rularea din terminal a unui fisier de teste specific: python -m unittest filename.py
    rularea din terminal a tuturor fisierelor de test: python -m unittest
    @unittest.skip plasat inaintea metodei de test - sare rularea testului respectiv
    wait implicit:
        chrome.implicitly wait(6)
    wait explicit:
        username =WebDriverWait(chrome, 3).until(EC.presence of element located(By.ID, "usernames")))
        username.send_keys("tomsmith")
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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



    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        #wait implicit
        #time.sleep(2)

    def tearDown(self) -> None:
        #time.sleep(1)
        self.driver.quit()

    def test_invalid_password(self):
        self.driver.implicitly_wait()
        # vrem sa probam accesul cu o parola gresita
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((self.USERNAME_SELECTOR)))
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)

        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.ID,'password')))
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.WRONG_PASSWORD)
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.LOGIN_SELECTOR))
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "Your password is invalid!\n×"
        #   sau
        assert "Your password is invalid" in self.driver.find_element(*self.ERROR_MESSAGE).text

        #assert self.driver.find_element(*self.ERROR_MESSAGE).get_attribute('class') == 'flash error'


        #time.sleep(1)
    @unittest.skip
    def test_invalid_user(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.WRONG_USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        #assert self.driver.find_element(*self.ERROR_MESSAGE).get_attribute('class') == 'flash error'
        #tema verificati mesajul de eroare primit cand se introduce un  username gresit
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "Your username is invalid!\n×"
        #   sau
        assert "Your username is invalid" in self.driver.find_element(*self.ERROR_MESSAGE).text
    def test_login_corect(self):
        self.driver.find_element(*self.USERNAME_SELECTOR).send_keys(self.USERNAME)
        self.driver.find_element(*self.PASSWORD_SELECTOR).send_keys(self.PASSWORD)
        self.driver.find_element(*self.LOGIN_SELECTOR).click()
        assert self.driver.find_element(*self.ERROR_MESSAGE).text == "You logged into a secure area!\n×"
        #assert self.driver.find_element(*self.SUCCESS_MESSAGE).get_attribute('class') == 'flash success'
        #print(self.driver.find_element(*self.LOGOUT_SELECTOR).get_attribute('class'))
        #assert self.driver.find_element(*self.LOGOUT_SELECTOR).get_attribute('class') == 'icon-2x icon-signout'
        assert 'icon-signout' in self.driver.find_element(*self.LOGOUT_SELECTOR).get_attribute('class')
        #time.sleep(2)

    #tema folositi wait implicit si explicit

