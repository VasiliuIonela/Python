import time

from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()
    driver.get("https://formy-project.herokuapp.com/form")
    time.sleep(3)
    #driver.find_element(By.ID, 'first-name').send_keys('Ionela')
    time.sleep(5)
    # driver.find_element(By.LINK_TEXT, 'Submit').click()
    # time.sleep(5)
    #driver.maximize_window()
    # driver.back()
    # my_bool = driver.find_element(By.CSS_SELECTOR, 'strong > label').is_displayed()
    # time.sleep(3)
    # print(f'Exista strong label in pagina noastra: {my_bool}.')
    # elemente = driver.find_elements(By.CLASS_NAME, 'form-control')
    # for element in elemente:
    #     print(element.text)
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Sub').click()
    # time.sleep(5)
    # driver.back()
    # 1. vom crea un xpath relativ care sa ne duca la primul input din formular
    element = driver.find_element(By.XPATH,"//input[@type='text']")
    print(f'element = {element.get_attribute("placeholder")}')

    #2. vom crea un xpath relativ care sa ne duca la primul input de tip text
    element = driver.find_element(By.XPATH, "//input[@type='text']")
    print(f'element = {element.get_attribute("placeholder")}')
    element = driver.find_element(By.XPATH, "//input[@id='first-name']")
    element.send_keys('Ionela')
    time.sleep(5)
    element = driver.find_element(By.XPATH, "//input[@id='first-name']//parent::div")
    assert driver.find_element(By.CSS_SELECTOR, 'strong > label').text == 'First name'

    #tema: folosind xpath anterior creati un nou xpath si printati textul label-ului din parintele div ->//input[@id='first-name']//parent::div/strong/label
    element = driver.find_element(By.XPATH, "//input[@id='first-name']//parent::div/strong/label")
    print(f'element = {element.text}')

    #tema: Explicati ce elemente identifica cei doi selectori xpath si care este diferenta dintre ei, cate rezultate returneaza fiecare?
    # //form/div/div/input
    #       - se navigheaza, folosind un xpath relativ, din parinte in copil.
    #       - se incepe din form si se identifica elementele  cu tag input
    #       - returneaza 4 rezultate
    elemente = driver.find_elements(By.XPATH, "//form/div/div/input")
    for element in elemente:
        print(f'elementul gasit = {element.get_attribute("placeholder")}')

    # //form//input
    #       - se navigheaza, folosind un xpath relativ, si se identifica toate elementele cu tag input
    #       - returneaza 10 rezultate
    elemente = driver.find_elements(By.XPATH, "//form//input")
    for element in elemente:
        print(f'-element gasit: {element.get_attribute("id")}')

    # tema: Identificati elementul cu id="radio-button-2 folosind un selector css si un selector xpath relativ si faceti click asupra lui.
    element = driver.find_element(By.CSS_SELECTOR,'input[id="radio-button-2"]').click()
    print(f's-a putut selecta radio button 2 ')
    time.sleep(3)

    element = driver.find_element(By.XPATH,'//input[@id="radio-button-2"]').click()
    print('ok')
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//form/div/div/div/input').click()
    time.sleep(4)





    #tema: Folosind pagina https://carturesti.ro/ explicati ce elemente identifica cei doi selectori //*[@class='ng-scope'] si .ng-scope
    # //*[@class='ng-scope'] returneaza toate elementele cu tag name-ul class ='ng-scope'; returneaza 1192 rezultate
    # driver.get("https://carturesti.ro/")
    # elements = driver.find_elements(By.XPATH, "//*[@class='ng-scope']")
    # nr_elemente =0
    # for element in elements:
    #     nr_elemente+=1
    # print(f'nr_rezultate pentru  xpath creat:  {nr_elemente}')
    print(f'lungime= {len(elements)}')

    # .ng-scope returneaza toate elementele in care se gaseste cuvantul:'ng-scope'; returneaza 1447 rezultate
    # elements = driver.find_elements(By.CSS_SELECTOR, ".ng-scope")
    # nr_elemente = 0
    # for element in elements:
    #     nr_elemente += 1
    # print(f'nr_rezultate pentru css selector creat:  {nr_elemente}')

    #acesta este raspunsul cand caut manual:
    #   nr_rezultate pentru  xpath creat:  1192
    #   nr_rezultate pentru css selector creat:  1447
    #acesta este raspunsul dupa compilare:
    #   nr_rezultate pentru  xpath creat:  1193
    #   nr_rezultate pentru css selector creat:  1445

finally:
    print('Eliberam resursa driver')
    driver.quit()
