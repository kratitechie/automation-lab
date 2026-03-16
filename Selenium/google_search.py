from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

text = "property in Indore"

for letter in text:
    search_box.send_keys(letter)
    time.sleep(0.2)

search_box.submit()

time.sleep(5)

driver.quit()