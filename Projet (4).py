#!/usr/bin/env python
# coding: utf-8

# # Cles pour la recherche

# In[19]:


voiture = {"MARQUE":str,"PRIX":[],"EMISIONS CO2":str,"ENERGIE":str,"BOITE":str,"PUISSANCE":[],"TYPE":str,"NB-PORTES":str or int,"NB-PLACE":str or int}


# # Fonctions pour les criteres de rechecher

# In[46]:


def critere():
    num = str(input("Voulez vous un critere d'emision de CO2 specifique ?: (Y/N)"))
    if(num == "Y"):
        print("1: A (> OU = A 100g/CO2/km)")
        print("2: B (DE 101 A 120 g/CO2/km)")
        print("3: C (DE 121 A 140 g/CO2/km)")
        print("4: D (DE 141 A 160 g/CO2/km)")
        print("5: E (DE 161 A 200 g/CO2/km)")
        print("6: F (DE 201 A 250 g/CO2/km)")
        print("7: G (< A 250 g/CO2/km)")
        print("8: PEUT-IMPORTE")
        crit = int(input())
        if (crit == 1):
            voiture["EMISIONS CO2"]= "A"
        if (crit == 2):
            voiture["EMISIONS CO2"]= "B"
        if (crit == 3):
            voiture["EMISIONS CO2"]= "C"
        if (crit == 4):
            voiture["EMISIONS CO2"]= "D"
        if (crit == 5):
            voiture["EMISIONS CO2"]= "E"
        if (crit == 6):
            voiture["EMISIONS CO2"]= "F"
        if (crit == 7):
            voiture["EMISIONS CO2"]= "G"
        if (crit == 8):
            voiture["EMISIONS CO2"]= "PEUT-IMPORTE"
    else:
        voiture["EMISIONS CO2"]= "PEUT-INMPORTE"
    return


# In[47]:


carburant = ['ESSENCE','GAZOIL','HYBRIDE','ELEC','PEUT-IMPORTE']


# In[48]:


def carbu():
    num = str(input("Voulez vous un type de motorisation specifique ?: (Y/N)"))
    if(num == "Y"):
        for i in range(len(carburant)):
            print( i," : ",carburant[i])
        crit = int(input())
        voiture["ENERGIE"]= carburant[crit]
    else:
        voiture["ENERGIE"]= "PEUT-INMPORTE"
    return


# In[49]:


ty = ["BERLINES","BREAK","MONOSPACE","CITADINES","CABRIOLETS/COUPE","PICKUP","4×4","CROSSOVERS","UTILITAIRE/FOURGONNETTES","SUV","PEUT-IMPORTE"]


# In[50]:


def types():
    num = str(input("Voulez vous un type de vehicule specifique: (Y/N)"))
    if(num == "Y"):
        for i in range(len(ty)):
            print( i," : ",ty[i])
        crit = int(input())
        voiture["TYPE"]= ty[crit]
    else:
        voiture["TYPE"]= "PEUT-INMPORTE"
    return


# In[51]:


pui1 = [[0,75],[70,80],[80,110],[110,130],[130,1000],["PEUT-IMPORTE"]]
pui2 = [[0,95],[95,110],[110,140],[140,180],[180,1000],["PEUT-IMPORTE"]]
pui3 = [[0,120],[120,140],[140,170],[170,200],[200,1000],["PEUT-IMPORTE"]]


# In[52]:


def puissance():
    num = str(input("Voulez vous une puissance specifique (Y/N)"))
    if(num == "Y"):
        if ((voiture["TYPE"]== "BERLINES") or (voiture["TYPE"]== "CITADINES") or(voiture["TYPE"]== "CABRIOLETS/COUPE")) :
            print("Quel est votre choix de puissance en tete sur ce proposer")
            for i in range(len(pui1)):
                print( i," : ",pui1[i]," ")
            crit = int(input())
            voiture["PUISSANCE"]= pui1[crit]
                
        if (voiture["TYPE"]== "BREAK"):
            print("Quel est votre choix de puissance en tete sur ce proposer")
            for i in range(len(pui2)):
                print( i," : ",pui2[i]," ")
            crit = int(input())
            voiture["PUISSANCE"]= pui2[crit]
        if ((voiture["TYPE"]== "MONOSPACE") or (voiture["TYPE"]== "PICKUP") or (voiture["TYPE"]== "4x4") or (voiture["TYPE"]== "CROSSOVERS") or (voiture["TYPE"]== "UTILITAIRE/FOURGONNETTES") or (voiture["TYPE"]== "SUV")):
            print("Quel est votre choix de puissance en tete sur ce proposer")
            for i in range(len(pui3)):
                print( i," : ",pui3[i]," ")
            crit = int(input())
            voiture["PUISSANCE"]= pui3[crit]
                
        if (voiture["TYPE"]== "PEUT-IMPORTE"):
                voiture["PUISSANCE"]= "PEUT-IMPORTE"       
    else:
        voiture["PUISSANCE"]= "PEUT-INMPORTE"
    
    return


# In[53]:


nbporte = [2,3,4,5,"PEUT-IMPORTE"]


# In[54]:


def porte():
    num = str(input("Voulez vous un nombre de porte specifique ?: (Y/N)"))
    if(num == "Y"):
        for i in range(len(nbporte)):
            print( i," : ",nbporte[i])
        crit = int(input("Choisiser le nombre de porte"))
        voiture["NB-PORTES"]= nbporte[crit]
    else:
        voiture["NB-PORTES"]= "PEUT-INMPORTE"
    return


# In[55]:


auto = ["Manuelle","Automatique","PEUT-IMPORTE"]


# In[65]:


def boite():
    num = str(input("Voulez vous une boite specifique ?: (Y/N)"))
    if(num == "Y"):
        for i in range(len(auto)):
            print( i," : ",auto[i])
        crit = int(input("Choisiser le type de boite"))
        voiture["BOITE"]= auto[crit]
    else:
        voiture["BOITE"]= "PEUT-INMPORTE"
    return


# In[66]:


nbplace = [2,3,4,5,6,7,8,9,"PEUT-IMPORTE"]


# In[67]:


def place():
    num = str(input("Voulez vous un nombre de place specifique ?: (Y/N)"))
    if(num == "Y"):
        for i in range(len(nbplace)):
            print( i," : ",nbplace[i])
        crit = int(input("Choisiser le nombre de place"))
        voiture["NB-PLACE"]= nbplace[crit]
    else:
        voiture["NB-PLACE"]= "PEUT-INMPORTE"
    return


# In[59]:


marques = ["Volkswagen","Seat","Skoda","Audi","Bentley","Lamborghini","Porsche","Toyota","Renault","Dacia","Nissan","Mitsubishi","Kia","Ford","Fiat","Chrysler","Alfa Romeo","Lancia","Abarth","Dodge","Jeep","Maserati","Chevrolet","Opel","Peugeot","Citroën","Suzuki","Nissan","DS","Hyundai","Mercedes-Benz","Mini","Volvo","Mazda","Smart","Honda","Jaguar","Land Rover","Subaru","Lexus","Tesla","Ferrari","PEUT-IMPORTE"]


# In[60]:


def marque():
    num = str(input("Voulez vous une marque specifique: (Y/N)"))
    if(num == "Y"):
        print("Avez vous une marque en tete sur ce proposer")
        for i in range(len(marques)):
            print( i," : ",marques[i])
        crit = int(input())
        voiture["MARQUE"]= marques[crit]
    else:
        voiture["MARQUE"]= "PEUT-INMPORTE"
    
    return 


# In[61]:


bude = [1,1]


# In[62]:


def budget():
    print("Quel est votre budget :")
    bud = int(input())
    bude[0]= bud
    bud = int(input())
    bude[1]= bud
    voiture["PRIX"]= bude
    return 


# # Fonction de recherche

# In[ ]:





# In[ ]:





# # Fonction d'excution de la recherche

# In[63]:


def choix():
    num = str(input("Voulez vous faire une recherche de voiture: (Y/N)"))
    while(num == "Y"):
        marque()
        budget()
        types()
        carbu()
        puissance()
        boite()
        critere()
        porte()
        place()
        print("Voici ce que vous avez choisi pour votre recherche","\n",voiture)
        a = str(input("Les critere vous convient: (Y/N)"))
        if(a=="Y"):
            
            
            num = str(input("voulez vous faire une autre rechecher avec d'autre critere: (Y/N)"))
    return 


# In[68]:


choix()


# In[ ]:





# In[ ]:





# In[ ]:




