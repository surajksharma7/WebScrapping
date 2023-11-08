# importing libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# initializing Service in a variable
s = Service()

driver = webdriver.Chrome(service=s) # initilizing the webbrowser and variable

driver.get('https://www.smartprix.com/mobiles')
time.sleep(3)

old_height = driver.execute_script('return document.body.scrollHeight')

while True:

    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div[1]/div[3]/div[3]').click()
    time.sleep(3)
    print(old_height)
    new_height = driver.execute_script('return document.body.scrollHeight')

    if old_height == new_height:
        break

    old_height = new_height

html = driver.page_source

with open('smartphone.html','w',encoding='utf-8') as f:
    f.write(html)