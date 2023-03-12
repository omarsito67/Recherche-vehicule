#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import re
import pickle


# In[3]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[4]:


def nb_modele(driver):
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[1]/div[2]/div/h2/strong').text
    return int(nombre)


# In[5]:


final_list_dacia=[]
liste_image_dacia=[]


# In[23]:


def modele_dacia():
    driver = webdriver.Chrome()
    driver.get("https://www.dacia.fr/achat-vehicules-neufs.html?colorMarketing.hexaCode=000000&energy.group=DIESEL%2CESS%2CELECTRIC&engine.powerOutputHp=45-110&transmission.group=MANUAL%2CAUTOMATIC&vehicleClassification=NC")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    accepter.click()
    #nombre = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[2]/h1').text
    #nombre_modele = int(''.join(filter(str.isdigit, nombre)))
    final_list_dacia=[]
    liste_image_dacia=[]
    for j in range(1,6):
        #if(j>=1 and j<=4):
        for i in range(1,25):
            if (j==1):
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/button/picture/img'.format(i))))
                    element = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/button/picture/img'.format(i))
                    image = element.get_attribute('src')            
                    liste_image_dacia.append(image)
                    print(image)
                    if(i%3!=0):
                        time.sleep(sleep_rand())
                        prix = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[1]/div[2]/div/span[2]'.format(i)).text
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[1]/div[1]/a/ul/li[2]'.format(i)).text                    
                except NoSuchElementException:
                       pass
            elif (j>1) :
                try :
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))))
                    element = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))
                    image = element.get_attribute('src')
                    liste_image_dacia.append(image)
                    print(image)
                    if(i%3!=0):
                        time.sleep(sleep_rand())
                        prix = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/div[1]/div[2]/div/span[2]'.format(i)).text
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/div[1]/div[1]/a/ul/li[2]'.format(i)).text                
                except NoSuchElementException:
                    pass
            time.sleep(sleep_rand())
            if(j==1):
                try:
                    modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[2]/button'.format(i))))
                    modele.click()
                    time.sleep(4)
                except NoSuchElementException:
                    pass
            else:
                try:
                    modele = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/div[2]/button'.format(i))))
                    modele.click()
                    time.sleep(4)
                except NoSuchElementException:
                    pass
            try:
                time.sleep(sleep_rand())
                caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[1]/div/h1').text
            except NoSuchElementException:
                try :
                    time.sleep(sleep_rand())
                    caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[2]/div[1]/div/h1').text      
                except NoSuchElementException:
                    pass
            if(i%3==0):
                try:
                    time.sleep(sleep_rand())
                    boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                except NoSuchElementException:
                    try:
                        time.sleep(sleep_rand())
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                    except NoSuchElementException:
                        pass
                try:
                    time.sleep(sleep_rand())
                    prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div').text
                except NoSuchElementException:
                    try:
                        prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div').text
                    except NoSuchElementException:
                        try:
                            prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div').text
                        except NoSuchElementException:
                            pass                                 
            if (boite=='Manuelle'):
                time.sleep(sleep_rand())
                try:
                    puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[6]/span').text 
                except NoSuchElementException:
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[6]/span').text 
                    except NoSuchElementException:
                        pass             
            else :
                time.sleep(sleep_rand())
                try:
                    puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[5]/span').text
                except NoSuchElementException:
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[5]/span').text
                    except NoSuchElementException:
                        pass
            time.sleep(2)
            #print(caracteristiques)
            #print(puissance)
            #print(prix)
            caract_nettoyage=caracteristiques.split("\n")
            puissance_chiffre=re.findall('(\d{3})',puissance)
            prix_chiffre=re.findall('(.*)_?€',prix)[0].replace('\u202f', ' ')
            prix_chiffre = int(prix_chiffre.replace(' ', ''))
            boite_carbu=re.findall('neuf - (.*) - Noir',caract_nettoyage[2])[0]
            if (boite_carbu=="100% électrique"):
                voiture={"modèle":caract_nettoyage[0]+" "+caract_nettoyage[1],"prix":prix_chiffre,"boîte de vitesse":boite,"puissance":int(puissance_chiffre[1]),"carburant":boite_carbu,"classe énergétique":'A'}   
            else:   
                voiture={"modèle":caract_nettoyage[0]+" "+caract_nettoyage[1],"prix":prix_chiffre,"boîte de vitesse":boite,"puissance":int(puissance_chiffre[1]),"carburant":"Essence","classe énergétique":caract_nettoyage[4]}                
            print(voiture)
            final_list_dacia.append(voiture)
            #print(final_list_dacia)
            #print(liste_image_dacia)
            time.sleep(sleep_rand())
            driver.back()
            time.sleep(4)
        
        if (j==5):
            break
        if(j==1):
            try :
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[{}]/button'.format(j+2))))
                page_suivante = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[{}]/button'.format(j+2))
                page_suivante.click()
            except NoSuchElementException:
                pass
        elif(j>1):    
            try :
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[{}]/button'.format(j+2))))
                page_suivante_1 = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[{}]/button'.format(j+2))
                page_suivante_1.click() 
            except NoSuchElementException:
                pass
        #elif(j>1) :
            #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[7]/button')))
            #page_suivante_1 = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[7]/button')
            #page_suivante_1.click()     
    return final_list_dacia,liste_image_dacia


# In[24]:


modele_dacia()


# In[74]:


# Enregistrement de la liste dans un fichier
with open("final_list_dacia.pickle", "wb") as f:
    pickle.dump(final_list_dacia, f)
with open("liste_image_dacia.pickle", "wb") as f:
    pickle.dump(liste_image_dacia, f)


# In[ ]:




