import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import csv

page = random.randint(1,50)

driver = webdriver.Chrome()

url = f"http://books.toscrape.com/catalogue/page-{page}.html"

print("Scraping page:", page)

driver.get(url)

time.sleep(1)

books = driver.find_elements(By.CLASS_NAME, "product_pod")[:5]

file_exists = os.path.exists("books.csv")

with open("books.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["Title", "Price"])

    for book in books:
        title = book.find_element(By.TAG_NAME, "h3") \
                    .find_element(By.TAG_NAME, "a") \
                    .get_attribute("title")

        price = book.find_element(By.CLASS_NAME, "price_color").text

        writer.writerow([title, price])