#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random


# In[69]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[70]:


def nb_modele(driver):
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[1]/div[2]/div/h2/strong').text
    return int(nombre)


# In[91]:


def modele_volks():
    driver = webdriver.Chrome()
    driver.get("https://www.volkswagen.fr/fr/configurateur.html?---=%7B%22filter-service%22%3A%22%2F%3FbodyType%3DCitadines%26bodyType%3DSportives%26bodyType%3DCabriolets%26bodyType%3DBerlines%26bodyType%3DBreaks%252FShooting%2BBrakes%26bodyType%3DSUV%26bodyType%3DMonospaces%26bodyType%3DUtilitaires%26engineType%3DEssence%26engineType%3DElectrique%26engineType%3DDiesel%26engineType%3DHybride%2Brechargeable%26gearType%3DAutomatique%26gearType%3DManuelle%22%7D")
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="bannerAcceptButton"]')
    accepter.click()
    wait = WebDriverWait(driver, 10)
    nombre_de_modele = nb_modele(driver)
    for i in range(1,nombre_de_modele+1):
        time.sleep(sleep_rand())
        modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[2]/ul/li[{}]/div[2]/div[2]/a'.format(i))))
        modele.click()
        nb_modele_local = nb_modele(driver)
        for j in range(1,nb_modele_local+1):
            #try:
                #quiter_aide = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="meetdeal-minimize-button-color"]')))
                #quiter_aide.click()
            #except NoSuchElementException:        
                #pass
            modele_local = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div/li/div[1]/div[2]/div[2]/a'.format(j))))
            modele_local.click()
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]')))
            time.sleep(sleep_rand())
            caracteristiques=driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]').text 
            prix= driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span').text
            element = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/div/div[1]/div[2]/img')
            image = element.get_attribute('src')
            print(caracteristiques)
            print(prix)
            print(image)
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


# In[93]:


modele_volks()


# In[ ]:


(/*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span)
(/*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span)
(/*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span)


# In[ ]:





# In[ ]:





# In[74]:


def modele_toyota():
    driver = webdriver.Chrome()
    driver.get("https://www.toyota.fr/vehicules-neufs")
    accepter = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    accepter.click()
    wait = WebDriverWait(driver, 10)
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="tor-cle8jrqrd26y716na3mbw92h0"]/div[3]/div[1]/div/div[1]/span[2]').text
    nombre_de_modele = int(nombre)
    for i in range(1,nombre_de_modele+1):
        modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tor-cle8jrqrd26y716na3mbw92h0"]/div[3]/div[2]/div[3]/article[{}]/button[2]'.format(i))))
        modele.click()
        time.sleep(4)
        nb_modele_v= wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="grade-selector-id"]/div[1]/div/div/div/div[1]/div/h3/span[1]').text))
        nb_modele = int(nb_modele_v)
        for j in range(1,nb_modele+1):
            caracteristiques=driver.find_element(by=By.XPATH, value='//*[@id="accordion-1548198877716847a5-6400-4002-a9a0-8d748df83b807b77d85b-8f26-4645-82ac-22154a7d6293"]/div[{}]]'.format(j)).text
            time.sleep(sleep_rand())
            #prix= driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[2]/div/div/div[3]/div[2]/div/div/div[1]/div[2]/span').text
            #image = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/div/div[1]/div[2]/img').pnj
            print(caracteristiques)
            #print(prix)
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
        exit = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[13]/div/div/button')))            
        exit.click()
    return


# In[76]:


modele_toyota()


# In[ ]:



(/*[@id="overflowable-gradeselector"]/div/ul/div/div/div[1])
(/*[@id="overflowable-gradeselector"]/div/ul/div/div/div[2])


# In[ ]:


'//*[@id="tor-cle7pi2uu1g2l16ojfrqs1npe"]/div[3]/div[2]/div[3]/article[1]/button[2]'


# In[ ]:


(/*[@id="tor-cle7pi2uu1g2l16ojfrqs1npe"]/div[3]/div[2]/div[3]/article[2]/button[2])


# In[82]:


def modele_dacia():
    driver = webdriver.Chrome()
    driver.get("https://www.dacia.fr/achat-vehicules-neufs.html?colorMarketing.hexaCode=000000&energy.group=DIESEL%2CESS%2CELECTRIC&engine.powerOutputHp=45-110&transmission.group=MANUAL%2CAUTOMATIC&vehicleClassification=NC")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    accepter.click()
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[2]/h1').text
    nombre_modele = int(''.join(filter(str.isdigit, nombre)))
    #print(nombre_modele)
    for i in range(1,nombre_modele+1):
        modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[2]/button'.format(i))))
        modele.click()
        time.sleep(4)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[1]/div/h1')))
        time.sleep(2)
        caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[1]/div/h1').text
        try:
            puissance = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[5]/span').text
        except NoSuchElementException:        
            puissance = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[6]/span').text
        #prix = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div/text()').text
        print(caracteristiques)
        print(puissance)
        #print(prix)
        time.sleep(sleep_rand())
        driver.back()
        time.sleep(4)


# In[52]:


modele_dacia()


# In[ ]:


#page 1
#//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[1]/div[2]/button
#//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[2]/div[2]/button
(/*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[24]/div[2]/button)
#page 2
#//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[1]/div[2]/button
#//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[2]/div[2]/button
#page 3
(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[1]/div[2]/button)
(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[1]/div[2]/button)
(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[24]/div[2]/button)

(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[1]/div[2]/button)
(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[24]/div[2]/button)

(/*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[19]/div[2]/button)
#bouton changer de page
#//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[7]/button

#nb de page
#//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[6]/button
#//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[8]/button

