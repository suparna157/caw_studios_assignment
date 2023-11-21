# This is a sample Python script.
import json
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

table_data = driver.find_element(By.XPATH, "//summary[contains(text(),'Table Data')]")
table_data.click()
time.sleep(2)
input_field = driver.find_element(By.XPATH, "//textarea[@id='jsondata']")
input_data = [{"name" : "Bob", "age" : 20, "gender": "male"}, {"name": "George", "age" : 42, "gender": "male"}, {"name":
"Sara", "age" : 42, "gender": "female"}, {"name": "Conor", "age" : 40, "gender": "male"}, {"name":
"Jennifer", "age" : 42, "gender": "female"}]
input_field.clear()
input_field.send_keys(json.dumps(input_data))
refresh_button = driver.find_element(By.XPATH, "//button[@id='refreshtable']")
refresh_button.click()



