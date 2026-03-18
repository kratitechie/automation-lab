"""
Script: google_search.py
Goal: Automate a Google search using Selenium.

Steps:
1. Launch Chrome
2. Navigate to Google
3. Locate search box using NAME locator
4. Type query
5. Submit search
"""



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("property in Indore")

search_box.submit()

time.sleep(5)

driver.quit()