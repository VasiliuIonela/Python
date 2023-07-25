from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.common import ElementNotInteractableException
import time
# def test_elefant_ro():
#     driver = webdriver.Chrome()
#     driver.get('https://www.elefant.ro/')
#     driver.maximize_window()
#     time.sleep(3)
#     #driver.find_element(By.CSS_SELECTOR, "button#CybotCookiesbotDialogBodyLevelButtonLevelOptionAllow")
#     try:
#         driver.find_element(By.CSS_SELECTOR, "button.close").click()
#     except ElementNotInteractableException:
#         pass
#     time.sleep(3)
#     try:
#         driver.find_element(By.CSS_SELECTOR, 'a.mobile-logo')
#         time.sleep(3)
#     except NoSuchElementException:
#         assert False, 'Elementul nu a fost gasit'
#     driver.quit()
#     print(f'Testul Elefant.ro Passed')

def test_cautare():
    driver = webdriver.Chrome()
    driver.get('https://www.elefant.ro/')
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,'[placeholder= "Căutați cuvânt cheie, codul de produs, tip produs"]').send_keys('Carti')
    driver.find_element(By.XPATH, "//button[@name='search']").is_selected()
    time.sleep(3)
    items_list = driver.find_elements(By.CSS_SELECTOR, '[class=\'product-title\']')
    time.sleep(2)
    driver.quit()
    assert len(items_list) >= 5, f'Lungimea listei este de {len(items_list)}'
    print('Test search bar passed')


def test_title():
    driver = webdriver.Chrome()
    driver.get('https://www.elefant.ro/')
    driver.maximize_window()
    assert driver.title==''


def test_login_wrong_credentials():
    #//span[contains(text(),'Cont')]
    driver = webdriver.Chrome()
    driver.get('https://www.elefant.ro/')
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[text()='Cont']").click()
    time.sleep(10)
    #a.my-account-login
    driver.find_element(By.CSS_SELECTOR, "a.my-account-login").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Email"]').send_keys('abc@.gmail.com')
    driver.find_element(By.CSS_SELECTOR, '[placeholder="Parola"]').send_keys('12345')
    driver.find_element(By.NAME, 'login').click()
#test_elefant_ro()


test_cautare()
#test_login_wrong_credentials()













