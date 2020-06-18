
#%%

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("C://Users/cluel/Documents/GitHub/Animal-Crossing-Popularity-Data/chromedriver.exe", chrome_options=options)

import time

url = 'https://www.animalcrossingportal.com/games/new-horizons/guides/villager-popularity-list.php'
driver.get(url)
classes = driver.find_elements_by_class_name("c-villager-name")

for x in range(len(classes)):
    if classes[x].is_displayed():
        driver.execute_script("arguments[0].click();", classes[x])
        time.sleep(2)
        
page_source = driver.page_source
#%%

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
villagers = []

print(soup)

#%%
tier_data = soup.find_all(class_="c-tier")
tier_list = list(tier_data)

villager_tier = []
villager_name = []
villager_rank = []
villager_message = []
villager_value = []

for i in tier_list:
    index = tier_list.index(i)
    tier = list(tier_list[index].find(class_="u-grow u-flex").find('p'))
    value = list(tier_list[index].find(class_="u-margin-left c-badge c-badge--gray"))
    villager_data = list(tier_list[index].find_all(class_="c-villager"))
    
    for i in villager_data:
        soup = villager_data[villager_data.index(i)]
        
        # Get Data
        villager_tier.append(tier[0])
        villager_value.append(value[0])
        villager_name.append(soup.find(class_="c-villager-name").get_text())
        villager_rank.append(soup.find(class_="c-villager-rank").get_text())
        
        # Reset Soup at End
        if villager_data[-1] == i:
            soup = BeautifulSoup(page_source, 'lxml')
#%%
        
# Create df
            
 #%%
            
# Get Table from Kaggle
            
            
# Connect to MySQL
            

# Upload Both Tables, Join together
        
        

# https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25