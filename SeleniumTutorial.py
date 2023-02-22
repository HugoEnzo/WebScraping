from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

url = "https://www.adamchoi.co.uk/overs/detailed"
path = "/Users/sivas/OneDrive/Desktop/WebScraping/chromedriver"

driver = webdriver.Chrome(path)
driver.get(url)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event = "All matches"]')
all_matches_button.click()

#Dropdown

dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away = []
for match in matches:
    date.append(match.find_element_by_xpath('./td[1]').text)
    home_team.append(match.find_element_by_xpath('./td[2]').text)

    #print(match.find_element_by_xpath('./td[2]').text)
    score.append(match.find_element_by_xpath('./td[3]').text)
    away.append(match.find_element_by_xpath('./td[4]').text)

driver.quit()

df = pd.DataFrame({
    'Date':date,
    'Home Team':home_team,
    'Score':score,
    'Away Team' : away
})
df.to_csv('football_data.csv', index = False)

print(df)