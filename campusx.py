from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

s = Service("C:/Users/Om Singh/Desktop/chromedriver.exe")

driver = webdriver.Chrome(service = s)


driver.get('https://www.smartprix.com/cameras')
time.sleep(2)

user_input = driver.find_element(by = By.XPATH, value = '//*[@id="app"]/main/div[1]/div[3]/div[2]/div[1]')
user_input.send_keys('CampusX')
time.sleep(1)

user_input.send_keys(Keys.ENTER)

link =  driver.find_element(by = By.XPATH, value = '//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3')
link.click()








time.sleep(50)