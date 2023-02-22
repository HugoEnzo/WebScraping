from selenium import webdriver
import pandas as pd
import time

web = "https://twitter.com/TwitterSupport"
path = "/Users/sivas/OneDrive/Desktop/WebScraping/chromedriver"

driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()
last_height = newHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    newHeight = driver.execute_script("return document.body.scrollHeight") 
    if newHeight==last_height:
        break
    else:
        last_height=newHeight