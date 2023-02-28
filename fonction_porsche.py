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
                        print(caract)
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
                        print(image)
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
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
                        caract=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div'.format(x)).text
                        time.sleep(sleep_rand())
                        print(caract)
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
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
                        print(caract)
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
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
                        print(caract)
                        try:
                            element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                            image = element.get_attribute('src')
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
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
                    print(caract)
                    try:
                        element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/img')
                        image = element.get_attribute('src')
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
                print(caract)
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
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
                print(caract)
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
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
                print(caract)
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
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
                print(caract)
                try:
                    element = driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[1]/div[{}]/div/div[2]/div/img'.format(x))
                    image = element.get_attribute('src')
                    print(image)
                except NoSuchElementException:
                    pass 
                if (x==19):
                    break
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')))
                fleche=driver.find_element(by=By.XPATH, value='//*[@id="modelexplorer"]/div[2]/div[2]/div[1]/div[4]')                 
                fleche.click()
            driver.back()
            
    return


# In[ ]:


modele_porsche()

