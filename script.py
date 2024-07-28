from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

url = "https://ci.cn/en/qqwl/qqky"
driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

country=[]
schoolname=[]
schoollink=[]
continent=[]

ul_element = driver.find_element(By.CSS_SELECTOR, "div.hd ul.island")
li_elements = ul_element.find_elements(By.TAG_NAME, "li")
for li in li_elements:
    li.click()
    print('clicked on :::::::::',li.text)
    time.sleep(5)
    count=driver.find_element(By.CSS_SELECTOR, "div.countries ul.country")
    countries=count.find_elements(By.TAG_NAME, "li")
#     print(countries)
#     countries=count.find_all('li')
#     print(countries)
    for c in countries:
        
#         print('clicked on ',c)
        c.click()
        print('clicked inside on::::::::',c.text)
        time.sleep(7)
        print('continent----',li.text)
        print('country -----',c.text)
        
#         print(li.text)
#         print('-----',c)
#         print(c.text)
#         soup= update_soup()
        s=driver.find_element(By.CSS_SELECTOR, "div.national ul.site-name")
        sc=s.find_elements(By.TAG_NAME, "li")
        for sn in sc:
            a_tag = sn.find_element(By.TAG_NAME, "a")
            link = a_tag.get_attribute("href")
            title = a_tag.text.strip()
            print('lnk of school',link)
            print('title of school',title)
            continent.append(li.text)
            country.append(c.text)
            schoollink.append(link)
            schoolname.append(title)
driver.quit()

df = pd.DataFrame({
    # 'Continent': continent,
    'Country': country,
    'School Name': schoolname,
    'School Url': schoollink
})     
df.to_csv('output_file.csv', index=False)