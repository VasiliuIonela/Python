import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")
#driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('Ionela') # # reprezinta id , . reprezinta class
# driver.find_elements(By.CSS_SELECTOR, 'input.form-control')[1].send_keys('Test')
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your job title']").send_keys('Tester')
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, 'div.input-group>div:nth-of-type(2) input').click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, 'div.input-group>div:last-of-type input').click()
# education_level = driver.find_element(By.CSS_SELECTOR, 'div.input-group>div:first-of-type label').text
# print(education_level)
# driver.find_element(By.CSS_SELECTOR, 'div.form-group > div:nth-of-type(2) > strong + input').send_keys('text')
# driver.find_element(By.XPATH, "//strong/following-sibling::input[@placeholder='Enter first name']").send_keys('Ceva')
# time.sleep(3)
# first_name=driver.find_element(By.XPATH, "//input/preceding-sibling::strong/label[@for='first-name']").text
# print(first_name)
# last_name = driver.find_element(By.XPATH, "//label[contains(text(),'Last name')]").text
# print(last_name)
driver.find_element(By.CSS_SELECTOR,'select#select-menu').click()
time.sleep(2)
driver.find_element(By.XPATH, '//option[@value=\'2\']').click()
time.sleep(2)
years_of_experience = Select(driver.find_element(By.CSS_SELECTOR,'select#select-menu'))
years_of_experience.select_by_index(1)
years_of_experience.select_by_value('3')
years_of_experience.select_by_visible_text('10+')
#driver.find_element(By.LINK_TEXT, 'Submit').click()
cautare = driver.find_element(By.CSS_SELECTOR,'input#first-name')
time.sleep(1)
cautare.send_keys('Ionela')
cautare2 = driver.find_elements(By.CSS_SELECTOR,'input#first-name')
cautare2[0].send_keys('Ionela')

time.sleep(5)
