from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = Options()
options.headless = False
#options.add_argument('window-size=1920x1080')


url = "https://www.audible.in/search"
driver_path = "/Users/sivas/OneDrive/Desktop/WebScraping/chromedriver"

driver = webdriver.Chrome(driver_path, options = options)
driver.get(url)
driver.maximize_window()


# / /div/@class = "adbl-impression-container"
#./li

#pagination

pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)


title = []
author_name = []
run_time = []

current_page = 1
while current_page<=last_page:
    time.sleep(2)
    container = WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.CLASS_NAME,"adbl-impression-container"))

    #container = driver.find_element_by_class_name('adbl-impression-container')
    products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located(By.CLASS_NAME,"productListItem"))
    #products = container.find_elements_by_xpath(".//li[contains(@class, 'productListItem')]")


    for product in products:
        #/ /h3[contains(@class = 'bc-heading')]
        title.append(product.find_element_by_xpath(".//h3[contains(@class,'bc-heading')]").text)
        author_name.append(product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
        print(product.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
        run_time.append(product.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)

    current_page+=1
    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass



driver.quit()

df = pd.DataFrame({
    "Title":title,
    "Author_Name":author_name,
    "Run_Time":run_time
})

df.to_csv("audible_scrape.csv", index = False)

print(df)
