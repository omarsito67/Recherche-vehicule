#!/usr/bin/env python
# coding: utf-8

# # Fichier à import

# In[146]:


import nbimporter
import pickle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# # Clé pour la recherche

# In[147]:


voiture = {"marque":str,"prix":[0,0],"boîte de vitesse":str,"puissance":[0,0],"carburant":str,"classe énergétique":str}


# # Fonctions pour les critères de recheche

# In[148]:


marques = ["Volkswagen","Dacia","Porsche","PEU IMPORTE"]


# In[149]:


def marque():
    num = str(input("Voulez-vous une marque spécifique ? (Y/N) "))
    if(num == "Y"):
        print("Avez-vous une préférence de marques sur celles proposées")
        for i in range(len(marques)):
            print( i," : ",marques[i])
        crit = int(input())
        voiture["marque"]= marques[crit]
    else:
        voiture["marque"]= "PEU IMPORTE"
    
    return 


# In[150]:


def budget():
    num = "N"
    while(num == "N"):
        bud = int(input("Quel est votre budget min : "))
        voiture["prix"][0] = bud
        bud = int(input("Quel est votre budget max : "))
        voiture["prix"][1] = bud
        print(voiture["prix"])
        num = str(input("Le budget vous convient-il ? (Y/N) "))
    return 


# In[151]:


auto = ["Manuelle","Automatique","PEU IMPORTE"]


# In[152]:


def boite():
    num = str(input("Voulez-vous une boîte de vitesse spécifique ? (Y/N) "))
    if(num == "Y"):
        for i in range(len(auto)):
            print( i," : ",auto[i])
        crit = int(input("Choisissez le type de boîtes de vitesse : "))
        voiture["boîte de vitesse"]= auto[crit]
    else:
        voiture["boîte de vitesse"]= "PEU IMPORTE"
    return


# In[153]:


def puissance():
    num = "N"
    while(num == "N"):
        bud = int(input("Quel est votre puissance min : "))
        voiture["puissance"][0] = bud
        bud = int(input("Quel est votre puissance max : "))
        voiture["puissance"][1] = bud
        print(voiture["puissance"])
        num = str(input("L'intervalle de puissance vous convient-il ? (Y/N) "))
    return


# In[154]:


carburant = ['Essence','Diesel','Hybride','100% électrique','PEU IMPORTE']


# In[155]:


def carbu():
    num = str(input("Voulez-vous un type de motorisation spécifique ? (Y/N) "))
    if(num == "Y"):
        for i in range(len(carburant)):
            print( i," : ",carburant[i])
        crit = int(input())
        voiture["carburant"]= carburant[crit]
    else:
        voiture["carburant"]= "PEU IMPORTE"
    return


# In[156]:


def critere():
    num = str(input("Voulez-vous un critère d'émision de CO² spécifique ? (Y/N) "))
    if(num == "Y"):
        print("1: A (> OU = A 100g/CO²/km)")
        print("2: B (DE 101 A 120 g/CO²/km)")
        print("3: C (DE 121 A 140 g/CO²/km)")
        print("4: D (DE 141 A 160 g/CO²/km)")
        print("5: E (DE 161 A 200 g/CO²/km)")
        print("6: F (DE 201 A 250 g/CO²/km)")
        print("7: G (< A 250 g/CO²/km)")
        print("8: PEUT-IMPORTE")
        crit = int(input())
        if (crit == 1):
            voiture["classe énergétique"]= "A"
        if (crit == 2):
            voiture["classe énergétique"]= "B"
        if (crit == 3):
            voiture["classe énergétique"]= "C"
        if (crit == 4):
            voiture["classe énergétique"]= "D"
        if (crit == 5):
            voiture["classe énergétique"]= "E"
        if (crit == 6):
            voiture["classe énergétique"]= "F"
        if (crit == 7):
            voiture["classe énergétique"]= "G"
        if (crit == 8):
            voiture["classe énergétique"]= "PEU IMPORTE"
    else:
        voiture["classe énergétique"]= "PEU IMPORTE"
    return


# # Fonction pour importer la base de données

# In[157]:


import pickle

# Ouverture du fichier contenant la liste caracteristique
#Volkswagen
with open("final_list_volks.pickle", "rb") as f:
    final_list_volks = pickle.load(f)
#Dacia
with open("final_list_dacia.pickle", "rb") as f:
    final_list_dacia = pickle.load(f)
#Porsche
with open("final_list_porsche.pickle", "rb") as f:
    final_list_porsche = pickle.load(f)

# Ouverture du fichier contenant la liste image
#Volkswagen
with open("liste_image_volks.pickle", "rb") as f:
    liste_image_volks = pickle.load(f)
#Dacia
with open("liste_image_dacia.pickle", "rb") as f:
    liste_image_dacia = pickle.load(f)
#Porsche
with open("liste_image_porsche.pickle", "rb") as f:
    liste_image_porsche = pickle.load(f)

#print(liste_image_porsche)


# # Fonction de tri de la base de données

# In[158]:


def liste_v(L1,L2):
    for i in range (0,(len(final_list_volks))):
            if(final_list_volks[i]["prix"]<=voiture["prix"][1] and final_list_volks[i]["prix"]>=voiture["prix"][0]):
                if((final_list_volks[i]["boîte de vitesse"]==voiture["boîte de vitesse"]) or (voiture["boîte de vitesse"]=="PEU IMPORTE")):
                    if(final_list_volks[i]["puissance"]<=voiture["puissance"][1] and final_list_volks[i]["puissance"]>=voiture["puissance"][0]):
                        if((final_list_volks[i]["carburant"]==voiture["carburant"]) or (voiture["carburant"]=="PEU IMPORTE")):
                            if((final_list_volks[i]["classe énergétique"]==voiture["classe énergétique"]) or (voiture["classe énergétique"]=="PEU IMPORTE")):
                                L1.append(final_list_volks[i])
                                L2.append(liste_image_volks[i])
    return


# In[159]:


def liste_d(L1,L2):
    for i in range (0,(len(final_list_dacia))):
            if(final_list_dacia[i]["prix"]<=voiture["prix"][1] and final_list_dacia[i]["prix"]>=voiture["prix"][0]):
                if((final_list_dacia[i]["boîte de vitesse"]==voiture["boîte de vitesse"]) or (voiture["boîte de vitesse"]=="PEU IMPORTE")):
                    if(final_list_dacia[i]["puissance"]<=voiture["puissance"][1] and final_list_dacia[i]["puissance"]>=voiture["puissance"][0]):
                        if((final_list_dacia[i]["carburant"]==voiture["carburant"]) or (voiture["carburant"]=="PEU IMPORTE")):
                            if((final_list_dacia[i]["classe énergétique"]==voiture["classe énergétique"]) or (voiture["classe énergétique"]=="PEU IMPORTE")):
                                L1.append(final_list_dacia[i])
                                L2.append(liste_image_dacia[i])
    return


# In[160]:


def liste_p(L1,L2):
    for i in range (0,(len(final_list_porsche))):
            if(final_list_porsche[i]["prix"]<=voiture["prix"][1] and final_list_porsche[i]["prix"]>=voiture["prix"][0]):
                if((final_list_porsche[i]["boîte de vitesse"]==voiture["boîte de vitesse"]) or (voiture["boîte de vitesse"]=="PEU IMPORTE")):
                    if(final_list_porsche[i]["puissance"]<=voiture["puissance"][1] and final_list_porsche[i]["puissance"]>=voiture["puissance"][0]):
                        if((final_list_porsche[i]["carburant"]==voiture["carburant"]) or (voiture["carburant"]=="PEU IMPORTE")):
                            if((final_list_porsche[i]["classe énergétique"]==voiture["classe énergétique"]) or (voiture["classe énergétique"]=="PEU IMPORTE")):
                                L1.append(final_list_porsche[i])
                                L2.append(liste_image_porsche[i])
    return


# In[161]:


liste_vehicule = []
liste_image_vehicule = []


# In[162]:


def recherche():
    liste_vehicule.clear()
    liste_image_vehicule.clear()
    if(voiture["marque"]=="Volkswagen"):
        liste_v(liste_vehicule,liste_image_vehicule)
    if(voiture["marque"]=="Dacia"):
        liste_d(liste_vehicule,liste_image_vehicule) 
    if(voiture["marque"]=="Porsche"):
        liste_p(liste_vehicule,liste_image_vehicule)
    else:
        liste_v(liste_vehicule,liste_image_vehicule)
        liste_d(liste_vehicule,liste_image_vehicule)
        liste_p(liste_vehicule,liste_image_vehicule)
    return


# # Code pour envoyer les résultats par email

# In[164]:


expediteur = 'autoscop.entreprise@gmail.com'
mot_de_passe = 'yweqwixhwakqqxjc'


# In[173]:


def mail():
    destinataire = str(input("Entre votre adresse mail: "))
    message = MIMEMultipart()
    message['Subject'] = 'Résultats de recherche AutoScope'
    message['From'] = expediteur
    message['To'] = destinataire
    liste_vehicules_str =[]
    if(len(liste_vehicule)==0):
        message_derreur ="""Bonjour,
        
L'équipe AutoScope vous remercie pour votre visite sur notre site. 
Votre recherche n'a pas pu aboutir faute d'offres correspondantes. 
Nous restons tous de même à disposition pour vos prochaines recherches. 

Bien cordialement, 
L'équipe Autoscope."""
        liste_vehicules_str.append(message_derreur) 
    else:
        body = """Bonjour,
L'équipe AutoScope vous remercie pour votre visite sur notre site et nous sommes ravis de vous présenter les résultats de votre recherche pour une voiture neuve correspondant à vos critères.

Nous avons trouvé les véhicules suivants :
"""
        end_message =  """
Nous espérons que ces résultats correspondent à vos attentes et répondent à vos besoins. N'hésitez pas à visiter notre site pour en savoir plus sur les autres véhicules disponibles.
Encore une fois, merci de nous faire confiance et n'hésitez pas à nous contacter si vous avez des questions.

Bien cordialement,
L'équipe AutoScope"""
        liste_vehicules_str.append(body)
        for i in range(len(liste_vehicule)):
            liste_vehicules_str.append("Modèle : "+liste_vehicule[i]['modèle'])
            liste_vehicules_str.append("Prix :"+ str(liste_vehicule[i]['prix']) +"€")
            liste_vehicules_str.append("Boîte de vitesse : "+liste_vehicule[i]['boîte de vitesse'])
            liste_vehicules_str.append("Puissance : "+str(liste_vehicule[i]['puissance'])+"CH")
            liste_vehicules_str.append("Carburant : "+liste_vehicule[i]['carburant'])
            liste_vehicules_str.append("Classe énergétique : "+liste_vehicule[i]['classe énergétique'])
            liste_vehicules_str.append("Image : "+liste_image_vehicule[i])
            liste_vehicules_str.append('\n')
        liste_vehicules_str.append(end_message)
    vehicules_str = '\n'.join(liste_vehicules_str)
    message.attach(MIMEText(vehicules_str))
    serveur_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    serveur_smtp.starttls()
    serveur_smtp.login(expediteur, mot_de_passe)
    serveur_smtp.sendmail(expediteur, destinataire, message.as_string())
    serveur_smtp.quit()
    return


# # Fonction d'exécution de la recherche

# In[166]:


def choix():
    num = str(input("Voulez-vous faire une recherche de voitures ? (Y/N) "))
    while(num == "Y"):
        marque()
        budget()
        boite()
        puissance()
        carbu()
        critere()
        print("Voici vos critères de recherche","\n",voiture)
        a = str(input("Les critères vous convient-ils ? (Y/N) "))
        if(a=="Y"):
            recherche()
            b = str(input("Voulez-vous que les résultats vous soient transmit par mail ? (Y/N) "))
            if(b=="Y"):
                mail()
            c = str(input("Voulez-vous que les résultats vous soient affiché ? (Y/N) "))
            if(c=="Y"):
                print(liste_vehicule)
                print(liste_image_vehicule)
            num = str(input("Voulez-vous faire une autre recheche avec d'autres critères ? (Y/N) "))
    return 


# In[167]:


choix()

