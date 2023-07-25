import time

from selenium import webdriver
from selenium.webdriver.common.by import By
def test_search_element():
    driver = webdriver.Chrome()
    driver.get("https://www.elefant.ro/")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "[placeholder ='Căutați cuvânt cheie, codul de produs, tip produs']").send_keys('Carti')
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@name='search']").is_selected()
    time.sleep(5)


    items_list = driver.find_elements(By.CSS_SELECTOR, "[class='product-title']")
    time.sleep(3)
    driver.quit()
    assert len(items_list) >=5, f'Lungimea listei rezultate in urma cautarii este de {len(items_list)}'
    print("Test search bar passed")

test_search_element()



