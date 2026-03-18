from selenium import webdriver
import csv
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer= csv.writer(f)
    writer.writerow(["Title", "Price"])
    
    for page in range(1,6):
        
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        print("Scraping page:", page)
        driver.get(url)
        time.sleep(3)
        
        books = driver.find_elements(By.CLASS_NAME, "product_pod")

        for book in books:
            
            title = book.find_element(By.TAG_NAME, "h3") \
                        .find_element(By.TAG_NAME, "a") \
                        .get_attribute("title")
            
            price = book.find_element(By.CLASS_NAME, "price_color").text
            
            writer.writerow([title, price])

driver.quit()