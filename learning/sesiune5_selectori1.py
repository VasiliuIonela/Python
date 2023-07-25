# inspect->ctr+F-pentru a putea cauta

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(3)
    driver.find_element(By.ID, 'first-name').send_keys('Ionela')
    #driver.find_element(By.ID, 'last-name').send_keys('Vasiliu')
    #driver.find_element(By.LINK_TEXT, 'Submit').click()
    time.sleep(3)
    #vedem optiuni de navigare ale driver-ului
    #maximizare fereaastra
    #driver.maximize_window()
    time.sleep(1)
    #driver.back()
    time.sleep(1)
    my_bool = driver.find_element(By.CSS_SELECTOR, 'strong > label').is_displayed()
    time.sleep(1)
    print(f'exista strong label in pagina noastra: {my_bool}')
    elemente = driver.find_elements(By.CLASS_NAME, 'form-control')
    #print(elemente) # elemente contine un tip de date propriu al selenium.
    #pentru a vedea o descriere a elemente care sa fie relevanta, putem folosi functia text
    # for element in elemente:
    #     print(element.text)
    # vrem sa identificam un link bazat pe un subset de caractere si sa dam click pe el
    #driver.find_element(By.PARTIAL_LINK_TEXT, 'Sub').click()
    time.sleep(5)
    # 1. vom crea un xpath relativ care sa ne duca la primul input din formular
    element = driver.find_element(By.XPATH,"//input")
    print(f'element = {element.get_attribute("placeholder")}')
    # 2. vom crea un xpath relativ care sa ne duca la primul input de tip text
    element = driver.find_element(By.XPATH,"//input[@type='text']")
    print(f'element = {element.get_attribute("placeholder")}')
    # element = driver.find_element(By.XPATH, "//input[@id='first-name']")
    # element.send_keys('Ionela')
    # time.sleep(5)
    #element = driver.find_element(By.XPATH, "//input[@id='first-name']//parent::div")

    #assert driver.find_element(By.CSS_SELECTOR,'strong > label').text == 'First name'


    #tema: folosind xpath anterior creati un nou xpath, si printati textul label-ului din parintele div



finally:
    print('Eliberam resursa driver')
    driver.quit()



