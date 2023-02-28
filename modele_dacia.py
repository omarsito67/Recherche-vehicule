#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.common.exceptions import NoSuchElementException


# In[ ]:


def sleep_rand():
    random_sleep = random.uniform(3,8)
    return random_sleep


# In[ ]:


def modele_dacia():
    driver = webdriver.Chrome()
    driver.get("https://www.dacia.fr/achat-vehicules-neufs.html?colorMarketing.hexaCode=000000&energy.group=DIESEL%2CESS%2CELECTRIC&engine.powerOutputHp=45-110&transmission.group=MANUAL%2CAUTOMATIC&vehicleClassification=NC")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')))
    accepter = driver.find_element(by=By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    accepter.click()
    nombre = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[2]/h1').text
    nombre_modele = int(''.join(filter(str.isdigit, nombre)))
    
    modele = []
    prix = []
    puissance = []
    consomation = []
    class_energetique = []
    image = []
        
    for j in range(1,6):
        if(j>=1 and j<=4):
            for i in range(1,25):
                if (j==1):
                    try:
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/button/picture/img'.format(i))))
                        element = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/button/picture/img'.format(i))
                        image = element.get_attribute('src')            
                        print(image)
                        if(i%3!=0):
                            prix = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[1]/div[2]/div/span[2]'.format(i)).text
                            boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div[{}]/div[1]/div[1]/a/ul/li[2]'.format(i)).text                    
                    except NoSuchElementException:
                        pass
                elif (j>1) :
                    try :
                        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))))
                        element = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))
                        image = element.get_attribute('src')
                        print(image)
                        if(i%3!=0):
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
                    caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[1]/div/h1').text
                    time.sleep(sleep_rand())
                except NoSuchElementException:
                    try :
                        caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[2]/div[1]/div/h1').text
                        time.sleep(sleep_rand())
                    except NoSuchElementException:
                        pass
                if(i%3==0):
                    try:
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                    except NoSuchElementException:
                        try:
                            boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                        except NoSuchElementException:
                            pass
                    try:
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
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[6]/span').text 
                    except NoSuchElementException:
                        try:
                            puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[6]/span').text 
                        except NoSuchElementException:
                            pass
                else :
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[5]/span').text
                    except NoSuchElementException:
                        try:
                            puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[5]/span').text
                        except NoSuchElementException:
                            pass
                time.sleep(2)

                print(caracteristiques)
                print(puissance)
                print(prix)
                time.sleep(sleep_rand())
                driver.back()
                time.sleep(4)
            if(j==1):
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[7]/button')))
                page_suivante = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[5]/div/ul/li[7]/button')
                page_suivante.click()
            elif(j>1) :
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[7]/button')))
                page_suivante_1 = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[4]/div/ul/li[7]/button')
                page_suivante_1.click() 
                
        elif(j==5):
            for i in range(1,15):
                try :
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))))
                    element = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button/picture/img'.format(i))
                    image = element.get_attribute('src')
                    print(image)
                    if(i%3!=0):
                        prix = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/div[1]/div[2]/div/span[2]'.format(i)).text
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/div[1]/div[1]/a/ul/li[2]'.format(i)).text                
                except NoSuchElementException:
                    pass
                
                time.sleep(sleep_rand())
                try:
                    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button'.format(i))))
                    modele=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/main/div[3]/div[{}]/button'.format(i))
                    modele.click()
                    time.sleep(4)
                except NoSuchElementException:
                    pass
                try:
                    caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[1]/div/h1').text
                    time.sleep(sleep_rand())
                except NoSuchElementException:
                    try :
                        caracteristiques = driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[2]/div[1]/div/h1').text
                        time.sleep(sleep_rand())
                    except NoSuchElementException:
                        pass
                if(i%3==0):
                    try:
                        boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                    except NoSuchElementException:
                        try:
                            boite=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[1]/div/ul/li[2]/div/p').text
                        except NoSuchElementException:
                            pass
                    try:
                        prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div[2]/div').text
                        time.sleep(sleep_rand())
                    except NoSuchElementException:
                        try:
                            prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div').text
                        except NoSuchElementException:
                            try:
                                prix=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[1]/div/div[2]/div[4]/div[1]/div[2]/div').text
                            except NoSuchElementException:
                                pass
                                              
                if (boite=='Manuelle'):
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[6]/span').text 
                    except NoSuchElementException:
                        try:
                            puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[6]/span').text 
                        except NoSuchElementException:
                            pass
                else :
                    try:
                        puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[2]/div[3]/div/div[2]/ul/li[5]/span').text
                    except NoSuchElementException:
                        try:
                            puissance=driver.find_element(by=By.XPATH, value='//*[@id="Page"]/div[3]/div[3]/div/div[2]/ul/li[5]/span').text
                        except NoSuchElementException:
                            pass
                time.sleep(2)

                print(caracteristiques)
                print(puissance)
                print(prix)
                time.sleep(sleep_rand())
                driver.back()
                time.sleep(4)            
    return


# In[ ]:


modele_dacia()

