#!/usr/bin/env python
# coding: utf-8

# In[57]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

def toyota():
    
    driver = webdriver.Safari()
    driver.get("https://www.toyota.fr")

    #PAUSE
    random_sleep = random.uniform(1, 5)
    time.sleep(random_sleep)
    
    #ACCEPTER COOKIE
    button1 = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    button1.click()

    #PAUSE
    random_sleep = random.uniform(1, 5)
    time.sleep(random_sleep)


    #VEHICULE NEUFS
    button2 = driver.find_element(By.XPATH, '//*[@id="cmp-top-navigation"]/nav/div[1]/div[2]/div[2]/ul/li[1]/a')
    button2.click()

    #PAUSE
    random_sleep = random.uniform(1, 5)
    time.sleep(random_sleep)

    #TOUS LES MODELES
    button3 = driver.find_element(By.XPATH, '//*[@id="navitemfirst-422ceda9-0270-4a5b-bdde-e01755e502cf"]/li[1]/div/a')
    button3.click()

    #PAUSE
    random_sleep = random.uniform(1, 5)
    time.sleep(random_sleep)

    button4 = driver.find_element(By.XPATH, '//*[@id="or-sidebar-wrapper"]/article/div[1]/details/summary/span[1]')
    button4.click()

    #PAUSE
    random_sleep = random.uniform(1, 5)
    time.sleep(random_sleep)

    
def choix_toyota():
    toyota()

choix_toyota()




# In[31]:


import requests
from bs4 import BeautifulSoup

url = "https://www.toyota.fr"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

element = soup.select_one("#myButton")



# In[ ]:




