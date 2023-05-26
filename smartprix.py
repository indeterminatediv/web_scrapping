from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('C:/Users/Om Singh/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service = s)

driver.get('https://www.smartprix.com/cameras')
time.sleep(10)


driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
time.sleep(2)
old_height = driver.execute_script('return document.body.scrollHeight')
try:
    while True:
        driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')

        print(new_height)
        print(old_height)

        if new_height == old_height:
            break
        old_height = new_height

except:
    pass

html = driver.page_source

with open('laptop.html','w', encoding='utf-8') as f:
    f.write(html)


















time.sleep(5)
