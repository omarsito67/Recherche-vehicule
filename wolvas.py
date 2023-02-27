#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random


# In[5]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[6]:


def nb_modele(driver):
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[1]/div[2]/div/h2/strong').text
    return int(nombre)


# In[110]:


def modele_volks():
    driver = webdriver.Chrome()
    driver.get("https://www.volkswagen.fr/fr/configurateur.html?---=%7B%22filter-service%22%3A%22%2F%3FbodyType%3DCitadines%26bodyType%3DSportives%26bodyType%3DCabriolets%26bodyType%3DBerlines%26bodyType%3DBreaks%252FShooting%2BBrakes%26bodyType%3DSUV%26bodyType%3DMonospaces%26bodyType%3DUtilitaires%26engineType%3DEssence%26engineType%3DElectrique%26engineType%3DDiesel%26engineType%3DHybride%2Brechargeable%26gearType%3DAutomatique%26gearType%3DManuelle%22%7D")
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="bannerAcceptButton"]')
    accepter.click()
    time.sleep(13)
    quiter_aide = driver.find_element(by=By.XPATH, value='//*[@id="meetdeal-minimize-button-color"]')
    quiter_aide.click()
    wait = WebDriverWait(driver, 10)
    nombre_de_modele = nb_modele(driver)
    for i in range(1,nombre_de_modele+1):
        time.sleep(sleep_rand())
        modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[2]/ul/li[{}]/div[2]/div[2]/a'.format(i))))
        modele.click()
        nb_modele_local = nb_modele(driver)
        for j in range(1,nb_modele_local+1):
            modele_local = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div/li/div[1]/div[2]/div[2]/a'.format(j))))
            modele_local.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]')))
            time.sleep(sleep_rand())
            caracteristiques=driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]').text 
            print(caracteristiques)
            prix= driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span').text
            print(prix)
            try:
                element = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/div/div[1]/div[2]/img')
                image = element.get_attribute('src')
                print(image)
            except NoSuchElementException:        
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/img')
                    image = element.get_attribute('src')
                    print(image)
                except NoSuchElementException:
                    pass
            time.sleep(sleep_rand())
            driver.back()
            time.sleep(4)
            suite = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/button')
            if(j == nb_modele_local):
                break
            else:
                if((j>1)and(j<nb_modele_local)):
                    for k in range(j):
                        suite.click()
                        time.sleep(2)
                    
        driver.back()
    return


# In[109]:


modele_volks()

