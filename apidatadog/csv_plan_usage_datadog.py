
from selenium import webdriver 
import time
import os
import shutil
nav= webdriver.Chrome()

nav.get('https://app.datadoghq.com/account/login')

time.sleep(3)

nav.find_element_by_xpath('//*[@id="username"]').send_keys("xxxxxxxxxxx")

nav.find_element_by_xpath('//*[@id="password"]').send_keys('xxxxxxxxxxxxxxxx')

nav.find_element_by_xpath('//*[@id="react-app"]/div/div[2]/div[1]/div[2]/div[6]/form/button').click()

time.sleep(2)

nav.get('https://app.datadoghq.com/billing/usage')



time.sleep(5)

nav.find_element_by_xpath('//*[@id="account_usage_usage_container"]/div[3]/div/div[1]/div[2]/div[1]/a').click()

time.sleep(10)



de = 'C:\\Users\\'

para = 'C:\\Users\\'




os.chdir(de)



for f in os.listdir():

  shutil.move(f, r'C:\\Users\\custo.csv')



time.sleep(5)



# outro ambiente

nav.get('https://app.datadoghq.com/api/v2/switch_to_user/cccbdef4-1288-11ed-ae92-da7ad0900002')


time.sleep(3)

nav.get('https://app.datadoghq.com/billing/usage')
time.sleep(4)
nav.find_element_by_xpath('//*[@id="account_usage_usage_container"]/div[3]/div/div[1]/div[2]/div[1]/a').click()
time.sleep(7)

os.chdir(de)

for g in os.listdir():
  shutil.move(g, r'C:\\Users\\custo2.csv')