#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import pickle


# In[2]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[16]:


final_list_porsche=[]
liste_image_porsche=[]


# In[17]:


def modele_porsche():
    
    driver = webdriver.Chrome() 
    driver.get("https://www.porsche.com/france/")
    
    wait = WebDriverWait(driver, 10)
    accepter = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="uc-sdk-banner-accept-all"]')))
    accepter.click()
    
    for i in range(1,7):
        
        time.sleep(sleep_rand())
        modele=wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/main/div[2]/div[1]/div/div[{}]/div[2]/div/div[2]/a[2]/span'.format(i))))
        time.sleep(sleep_rand())
        modele.click()
        
        if(i==1):
            for j in range(4):
                if(j==0):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s718-models"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    
                    for x in range(1,11):
                        time.sleep(sleep_rand())
                        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                        time.sleep(2)
                        caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                        time.sleep(sleep_rand())
                                        
                        caract_nettoyage=caract.split("\n")
                        
                        if(caract_nettoyage[0]=='Nouveau'):
                            caract_nettoyage.remove(caract_nettoyage[0])
                        puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                        prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                        prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                        
                        for y in range(11,18):
                            crit=" ".join(caract_nettoyage[y])
                            if(len(crit)>1):
                                classe_energie=crit[0]
                        
                        voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}

                        #print(caract)
                        print(voiture)
                        final_list_porsche.append(voiture)
                        
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
                            liste_image_porsche.append(image)
                            print(image)
                        except NoSuchElementException:
                            pass
                        if (x==10):
                            break
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                        fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')
                        fleche.click()
                    driver.back()
                if(j==1):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s718-cayman-gt4"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                    
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])                    
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)
                    
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        print(image)
                        liste_image_porsche.append(image)
                    except NoSuchElementException:
                        pass
                    driver.back()
                if(j==2):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s718-spyder"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                    
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])                    
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)                    
                    
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        liste_image_porsche.append(image)
                        print(image)
                    except NoSuchElementException:
                        pass                    
                    driver.back()
                
                if(j==3):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s718-cayman-gt4-rs"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                    
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)                    
                    
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        liste_image_porsche.append(image)
                        print(image)
                    except NoSuchElementException:
                        pass                    
                    driver.back()
            driver.back()
        
        if(i==2):
            for j in range(6):
                if(j==0):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-models"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    for x in range(1,18):
                        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                        time.sleep(2)
                        try:
                            caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                        except NoSuchElementException:
                            pass
                        
                        time.sleep(sleep_rand())
                        #print(caract)
                        
                        caract_nettoyage=caract.split("\n")
                        if(caract_nettoyage[0]=='Nouveau'):
                            caract_nettoyage.remove(caract_nettoyage[0])
                        puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                        prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                        prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                        for y in range(11,18):
                            crit=" ".join(caract_nettoyage[y])
                            if(len(crit)>1):
                                classe_energie=crit[0]
                        voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                        print(voiture)
                        final_list_porsche.append(voiture)                        
                        
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
                            liste_image_porsche.append(image)
                            print(image)
                        except NoSuchElementException:
                            pass                        
                        if (x==17):
                            break
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                        fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                        
                        fleche.click()
                    driver.back()
                
                if(j==1):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-turbo-models"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    for x in range(1,5):
                        time.sleep(sleep_rand())
                        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                        time.sleep(2)
                        caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                        time.sleep(sleep_rand())
                        #print(caract)
                        
                        caract_nettoyage=caract.split("\n")
                        if(caract_nettoyage[0]=='Nouveau'):
                            caract_nettoyage.remove(caract_nettoyage[0])
                        puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                        prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                        prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                        for y in range(11,18):
                            crit=" ".join(caract_nettoyage[y])
                            if(len(crit)>1):
                                classe_energie=crit[0]
                        voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                        print(voiture)
                        final_list_porsche.append(voiture)                         
                        
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
                            liste_image_porsche.append(image)
                            print(image)
                        except NoSuchElementException:
                            pass                          
                        if (x==4):
                            break
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                        fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                        
                        fleche.click()
                    driver.back()
                        
                if(j==2):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-gt3-models"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    for x in range(1,3):
                        time.sleep(sleep_rand())
                        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div'.format(x))))
                        time.sleep(2)
                        caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div'.format(x)).text
                        time.sleep(sleep_rand())
                        #print(caract)
                        
                        caract_nettoyage=caract.split("\n")
                        if(caract_nettoyage[0]=='Nouveau'):
                            caract_nettoyage.remove(caract_nettoyage[0])
                        puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                        prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                        prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                        for y in range(11,18):
                            crit=" ".join(caract_nettoyage[y])
                            if(len(crit)>1):
                                classe_energie=crit[0]
                        voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                        print(voiture)
                        final_list_porsche.append(voiture)                         
                        
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
                            liste_image_porsche.append(image)
                            print(image)
                        except NoSuchElementException:
                            pass                       
                        if (x==2):
                            break
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div/div[1]/div[4]')))
                        fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[4]')                        
                        fleche.click()
                    driver.back()
                
                if(j==3):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-gt3-rs"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                        
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)                     
                    
                    time.sleep(sleep_rand())
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        liste_image_porsche.append(image)
                        print(image)
                    except NoSuchElementException:
                        pass                    
                    driver.back()
                
                if(j==4):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-sport-classic"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                    
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)                     
                    
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        liste_image_porsche.append(image)
                        print(image)
                    except NoSuchElementException:
                        pass                    
                    driver.back()
                
                if(j==5):
                    sous_modele=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="s911-dakar"]')))
                    sous_modele.click()
                    time.sleep(sleep_rand())
                    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div')))
                    time.sleep(2)
                    caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div').text
                    time.sleep(sleep_rand())
                    #print(caract)
                    
                    caract_nettoyage=caract.split("\n")
                    if(caract_nettoyage[0]=='Nouveau'):
                        caract_nettoyage.remove(caract_nettoyage[0])
                    puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                    prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                    prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                    voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                    print(voiture)
                    final_list_porsche.append(voiture)                     
                    
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        liste_image_porsche.append(image)
                        print(image)
                    except NoSuchElementException:
                        pass                    
                    driver.back()
            driver.back()
        if(i==3):
            for x in range(1,15):
                time.sleep(sleep_rand())
                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                time.sleep(2)
                caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                time.sleep(sleep_rand())
                #print(caract)
                
                caract_nettoyage=caract.split("\n")
                if(caract_nettoyage[0]=='Nouveau'):
                    caract_nettoyage.remove(caract_nettoyage[0])
                puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[4])[0]
                prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))

                voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'100% électrique',"classe énergétique":'A'}
                print(voiture)
                final_list_porsche.append(voiture)                 
                
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
                    liste_image_porsche.append(image)
                    print(image)
                except NoSuchElementException:
                    pass                 
                if (x==14):
                    break
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                 
                fleche.click()
            driver.back()
        if(i==4):
            for x in range(1,26):
                time.sleep(sleep_rand())
                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                time.sleep(2)
                caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                time.sleep(sleep_rand())
                #print(caract)
                
                caract_nettoyage=caract.split("\n")
                if(caract_nettoyage[0]=='Nouveau'):
                    caract_nettoyage.remove(caract_nettoyage[0])
                puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                
                if ((caract_nettoyage[10]=='l/100 km') and (caract_nettoyage[12]=='kWh/100 km')):
                    carbu='Hybride'
                    classe_energie='A'
                elif (caract_nettoyage[10]=='kWh/100 km'):
                    carbu='100% électrique'
                    classe_energie='A'
                elif (caract_nettoyage[10]=='l/100 km'):
                    carbu='Essence'
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]

                voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":carbu,"classe énergétique":classe_energie}
                print(voiture)
                final_list_porsche.append(voiture)                  
                
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
                    liste_image_porsche.append(image)
                    print(image)
                except NoSuchElementException:
                    pass 
                if (x==25):
                    break
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                 
                fleche.click()
            driver.back()
        if(i==5):
            for x in range(1,5):
                time.sleep(sleep_rand())
                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div'.format(x))))
                time.sleep(2)
                caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div'.format(x)).text
                time.sleep(sleep_rand())
                #print(caract)
                
                caract_nettoyage=caract.split("\n")
                if(caract_nettoyage[0]=='Nouveau'):
                    caract_nettoyage.remove(caract_nettoyage[0])
                puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                
                for y in range(11,18):
                    crit=" ".join(caract_nettoyage[y])
                    if(len(crit)>1):
                        classe_energie=crit[0]
                voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":'Essence',"classe énergétique":classe_energie}
                print(voiture)
                final_list_porsche.append(voiture)                  
                
                time.sleep(sleep_rand())
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
                    liste_image_porsche.append(image)
                    print(image)
                except NoSuchElementException:
                    pass 
                if (x==4):
                    break
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div/div[1]/div[4]')))
                fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[4]')                 
                fleche.click()
            driver.back()            
        if(i==6):
            for x in range(1,20):
                time.sleep(sleep_rand())
                wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x))))
                time.sleep(2)
                caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                time.sleep(sleep_rand())
                #print(caract)
                
                caract_nettoyage=caract.split("\n")
                if(caract_nettoyage[0]=='Nouveau'):
                    caract_nettoyage.remove(caract_nettoyage[0])
                puissance_chiffre=re.findall('/(.*) ch',caract_nettoyage[2])[0]
                prix_chiffre=re.findall('EUR (.*) TTC',caract_nettoyage[1])[0]
                prix_chiffre = int(prix_chiffre.replace(' ', '').replace(',', ''))
                
                if ((caract_nettoyage[10]=='l/100 km') and (caract_nettoyage[12]=='kWh/100 km')):
                    carbu='Hybride'
                    classe_energie='A'
                elif (caract_nettoyage[10]=='kWh/100 km'):
                    carbu='100% électrique'
                    classe_energie='A'
                elif (caract_nettoyage[10]=='l/100 km'):
                    carbu='Essence'
                    for y in range(11,18):
                        crit=" ".join(caract_nettoyage[y])
                        if(len(crit)>1):
                            classe_energie=crit[0]
                voiture={"modèle":caract_nettoyage[0],"prix":prix_chiffre//100,"boîte de vitesse":'Automatique',"puissance":int(puissance_chiffre),"carburant":carbu,"classe énergétique":classe_energie}
                print(voiture)
                final_list_porsche.append(voiture)                  
                
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
                    liste_image_porsche.append(image)
                    print(image)
                except NoSuchElementException:
                    pass 
                if (x==19):
                    break
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                 
                fleche.click()
            driver.back()
            
    return final_list_porsche, liste_image_porsche


# In[19]:


modele_porsche()


# In[21]:


# Enregistrement de la liste dans un fichier
with open("final_list_porsche.pickle", "wb") as f:
    pickle.dump(final_list_porsche, f)
with open("liste_image_porsche.pickle", "wb") as f:
    pickle.dump(liste_image_porsche, f)

