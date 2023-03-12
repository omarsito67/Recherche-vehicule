#!/usr/bin/env python
# coding: utf-8

# In[94]:


import requests
import re
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import pickle


# In[95]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[96]:


def nb_modele(driver):
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div[2]/div/div[1]/div[2]/div/h2/strong').text
    return int(nombre)


# In[97]:


final_list_volks=[]
liste_image_volks=[]


# In[98]:


def modele_volks():
    driver = webdriver.Chrome()
    driver.get("https://www.volkswagen.fr/fr/configurateur.html?---=%7B%22filter-service%22%3A%22%2F%3FbodyType%3DCitadines%26bodyType%3DSportives%26bodyType%3DCabriolets%26bodyType%3DBerlines%26bodyType%3DBreaks%252FShooting%2BBrakes%26bodyType%3DSUV%26bodyType%3DMonospaces%26bodyType%3DUtilitaires%26engineType%3DEssence%26engineType%3DElectrique%26engineType%3DDiesel%26engineType%3DHybride%2Brechargeable%26gearType%3DAutomatique%26gearType%3DManuelle%22%7D")
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="bannerAcceptButton"]')
    accepter.click()
    time.sleep(13)
    try:
        quiter_aide = driver.find_element(by=By.XPATH, value='//*[@id="meetdeal-minimize-button-color"]')
        quiter_aide.click()
    except NoSuchElementException:
        pass
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
            time.sleep(sleep_rand())
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]')))
            time.sleep(sleep_rand())
            caracteristiques=driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div/section[2]/div/div/div[2]/div[1]/div[2]').text
            if caracteristiques.find("GTE") != -1:
                cara = caracteristiques.split(';')
                model=""
                for caractere in cara[0]:
                    if not caractere.isdigit():
                        model += caractere
                    else:
                        break
                model.strip()
                carbu = "Hybride"
                Boite = "Automatique"
                pp = re.search(r'\b(\d+)\s*CH\b', cara[0])
                puissance = int(pp.group(1))
                classe_energetique = cara[5].split('\n')[1]
            else:
                cara = caracteristiques.split(';')
                if cara[0].find("BVM") != -1:
                    Boite = "Manuelle"
                else:
                    Boite = "Automatique"
                carbu = cara[1].replace(" ", "")
                pp = re.search(r'\b(\d+)\s*CH\b', cara[0])
                puissance = int(pp.group(1))
                model=""
                for caractere in cara[0]:
                    if not caractere.isdigit():
                        model += caractere
                    else:
                        break
                model.strip()
                classe_energetique = cara[3].split('\n')[1]
            try:
                price= driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div[2]/div/div/div[1]/div[2]/span').text
            except NoSuchElementException: 
                price= driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/footer/div/div/div/div[1]/div[2]').text
            prix = int(''.join(filter(str.isdigit, price)))
            voiture={"modèle":model,"prix":prix,"boîte de vitesse":Boite,"puissance":puissance,"carburant":carbu,"classe énergétique":classe_energetique}
            print(voiture)
            final_list_volks.append(voiture)
            try:
                element = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/div/div[1]/div[2]/img')
                image = element.get_attribute('src')
                liste_image_volks.append(image)
                print(image)
            except NoSuchElementException:        
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="MOFA"]/div/div/div/div/div/div/div/div[2]/section[1]/div/div/div/div/div/img')
                    image = element.get_attribute('src')
                    liste_image_volks.append(image)
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
    return(final_list_volks,liste_image_volks)


# In[99]:


modele_volks()


# In[100]:


# Enregistrement de la liste dans un fichier
with open("final_list_volks.pickle", "wb") as f:
    pickle.dump(final_list_volks, f)
with open("liste_image_volks.pickle", "wb") as f:
    pickle.dump(liste_image_volks, f)

