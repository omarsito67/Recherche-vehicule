# Projet AutoScope

Dans le cadre de la réalisation de notre projet d’automatisation en python nous avons fait le choix de créer un outil pour faciliter la recherche de voiture neuve pour un client. 
Pour ce faire nous avons décidé de mettre au point AutoScope, le but de cet outil est de scraper différentes page web de marques de voitures, récupérer les données sur les différentes voitures disponible en stock tel que : Le modèle, la puissance, le prix, la classe énergétique, l’image etc
Par la suite les données récolté seront stocké dans des dataframe de manière adéquate. L’utilisateur ou le client pourra entrer ses différents critères et il lui seront alors proposé les modèles correspondant.

Ici sera présenté la version 1.0 d’AutoScope, encore en version d’essai. 
Cette version réuni les modèles pour les trois marques suivantes : Dacia, Volkswagen et Porsche.
Les données récolté sont les suivantes : Prix, Modèle, Puissance, Classe énergétique, Image, Boîte ( manuelle ou automatique ) et une donnée sur le carburant ( Electrique, essence, diesel ou hybride ). 

La présentation du code sera découpé en quatre partie pour faciliter la compréhension :
Partie 1 : WebScraping pour Volkswagen
Partie 2 : WebScraping pour Dacia
Partie 3 : WebScraping pour Porsche
Partie 4 : Fonction de l’utilisateur
