from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from time import sleep

url = "https://www.coronatracker.com/pt-br"

driver = webdriver.Chrome()
driver.get(url)
sleep(3)

casos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
casostext = casos.text

print(casostext)