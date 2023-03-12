# Projet AutoScope

Dans le cadre de la réalisation de notre projet d’automatisation en python nous avons fait le choix de créer un outil pour faciliter la recherche de voiture neuve pour un client. 

Pour ce faire nous avons décidé de mettre au point AutoScope, le but de cet outil est de scraper différentes page web de marques de voitures, récupérer les données sur les différentes voitures disponible en stock tel que : Le modèle, la puissance, le prix, la classe énergétique, l’image etc

Par la suite les données récolté seront stocké dans des dataframe de manière adéquate. L’utilisateur ou le client pourra entrer ses différents critères et il lui seront alors proposé les modèles correspondant. De plus il lui sera proposé en fin de recherche s'il souhaite recvoir un mail récapitulatif de sa recherche. Et tous cela sera s'ajoutera une interface web.



Ici sera présenté la version 1.0 d’AutoScope, encore en version d’essai. 

Cette version réuni les modèles pour les trois marques suivantes : Dacia, Volkswagen et Porsche.

Les données récolté sont les suivantes : Prix, Modèle, Puissance, Classe énergétique, Image, Boîte ( manuelle ou automatique ) et une donnée sur le carburant ( Electrique, essence, diesel ou hybride ).



# La présentation du code sera découpé en plusieurs parties pour faciliter la compréhension :

Partie 1 : WebScraping pour Volkswagen. 

Partie 2 : WebScraping pour Dacia. 

Partie 3 : WebScraping pour Porsche. 

Partie 4 : Fonction de l’utilisateur. 

Partie 5 : Mail récapitulatif.      

Partie 6 : Interface web. 



# Partie 1/2/3:

Les fichiers suivants "wolvas.py", "porsche.py" et "modele_dacia.py" regroupent les 3 premières parties, le WebScraping. Pour ce faire, nous avons commencé par accéder à la page et accepter les cookies. Ensuite, nous avons fermé la fenêtre d'aide si elle était affichée. Nous avons également récupéré le nombre de pages et le nombre de modèles de voitures disponibles sur chaque page à l'aide de Xpath. Nous avons mis ces informations dans des boucles pour parcourir toutes les pages et extraire les données de chaque modèle de voiture.Pour extraire les données, nous avons utilisé la méthode split pour traiter les chaînes de caractères et stocker les données dans des dataframes. Les données ont été stockées sous forme de listes, car il était impossible d'attendre une heure à chaque fois pour récupérer les listes et effectuer une recherche. Il convient de noter que notre outil doit être mis à jour régulièrement, car de nouveaux modèles apparaissent fréquemment et le code de la page peut également être modifié. Ces limites sont claires pour notre outil.
En résumé, nous avons utilisé Selenium pour accéder à une page web, accepter les cookies, fermer la fenêtre d'aide, extraire les données sur les modèles de voitures et les stocker dans des dataframes. Nous avons également noté que notre outil doit être mis à jour régulièrement pour rester efficace.

# Partie 4:

La fonction de l'utilisateur se trouve dans le fichier suivant "Projet.py", qui regroupe plusieurs fonctions. Au début, nous avons créé 6 fonctions qui, une fois appelées, demandent à l'utilisateur d'entrer ses critères de recherche tels que la marque, le budget, la puissance, la classe énergétique, la boîte et le carburant. Nous avons ensuite utilisé pickle pour ouvrir les listes précédemment enregistrées. Ensuite, nous avons défini trois fonctions qui vont trier les véhicules en fonction de la marque. Nous avons également défini deux listes vides pour les critères et les images, qui seront remplies à chaque fois qu'un modèle correspond à la recherche de l'utilisateur. Enfin, nous avons défini une fonction de recherche qui permettra à l'utilisateur de rechercher des modèles en fonction de ses critères. Cette fonction va d'abord regarder quel est la marque choisi, ensuite, la fonction de recherche va parcourir les modèles pour vérifier s'ils correspondent aux critères de l'utilisateur. Chaque fois qu'un modèle correspond, les critères et les images correspondants seront ajoutés aux listes vides définies précédemment.

# Partie 5:

La fonction pour envoyer un mail récapitulatif se trouve aussi dans ce fichier, on commence par définir qui sera l'expéditeur du mail, en l'occurrence AutoScope. Nous avons également créé une fonction "mail" qui permet à l'utilisateur d'entrer son adresse mail. Pour créer le message, nous avons utilisé la classe myMultipart pour structurer le message. Nous avons ensuite défini une liste de chaînes de caractères pour le message. Si cette liste est vide, un message d'erreur sera affiché. Nous avons commencé par créer le corps du message, qui contient le message de bienvenue qui apparaît en premier. Ensuite, pour chaque élément de la liste, nous avons ajouté un élément au message en utilisant "\n" pour créer un retour à la ligne et rendre le message plus propre. Enfin, nous avons généré les modèles en ajoutant les détails des critères pour chaque modèle. À la fin du message, nous avons affiché un message de fin.
En résumé, nous avons créé une fonction "mail" qui permet à l'utilisateur d'entrer son adresse mail. Nous avons utilisé la classe myMultipart pour structurer le message et avons défini une liste de chaînes de caractères pour le message. Nous avons créé le corps du message, puis ajouté chaque élément de la liste au message avec un retour à la ligne pour un rendu plus propre. Nous avons ensuite ajouté les détails des critères pour chaque modèle avant d'afficher un message de fin.
Ensuite on definit la fonction choix() qui va demander à l'utilisateur s'il souhaite effectuer une recherche. Si oui, elle va exécuter toutes les fonctions de critères et demander à l'utilisateur si les résultats correspondent à ses critères. Si non, elle recommence le processus de recherche. Si oui, elle lance la fonction "Recherche" qui trie les listes en fonction des critères. Ensuite, on demande à l'utilisateur s'il souhaite recevoir les résultats par mail. Si oui, on lance la fonction "mail". Si non, on demande à l'utilisateur s'il souhaite afficher les résultats. Si oui, on print les deux listes. Si non, on passe cette étape. Enfin, on demande à l'utilisateur s'il souhaite effectuer une autre recherche. Si oui, on relance le processus de recherche. Si non, on quitte le programme.

# Partie 6:

Nous avons voulu créer une interface web pour notre outil de recherche. Cependant, en raison de nos connaissances limitées en matière de développement web, nous n'avons pas été en mesure de créer une interface fonctionnelle. Nous avons toutefois créé un aperçu de ce à quoi pourrait ressembler notre page web.
Dans le fichier "..." se trouve notre code HTML et CSS. Dans notre HTML, nous avons utilisé plusieurs liens Bootstrap qui nous ont été utiles pour rendre la page responsive et ne pas avoir à créer de flexbox, ajouter des classes prédéfinies de couleur et donc "styliser" notre page en utilisant des regles CSS pré-écrite etc. Le reste du code HTML a été réalisé en reprenant le code d'une autre page web réalisée en licence.

# Les difficultés rencontrées:

Choix entre Selenium et Beautiful Soup
Code variant en fonction des pages
Inspection de nombreux sites avant de sélectionner les marques à scraper
Boutons avec Xpath erronés
Récupération des données en masse avec un même Xpath, nécessitant un découpage et une séparation
Idée initiale d'un site complet avec une interface fonctionnelle et un choix de marques et modèles plus large, ce qui a demandé plus de temps
Réflexion ultérieure pour récupérer l'Xpath de chaque donnée et stocker directement pour éviter le nettoyage excessif
Manque de documentation pour certaines pages

# Pour aller plus loin...

Création d'une interface web pour faciliter l'utilisation de notre service. Soit en dynamisant avec du JavaScrpit ou en passant via Django.
Ajout de plus de données en scrapant davantage de sites pour offrir un choix encore plus large aux utilisateurs.
Ajout de critères de recherche supplémentaires pour affiner les résultats.
Affichage des véhicules les plus recherchés ou les plus vendus pour aider les utilisateurs dans leur choix.
Redirection de l'utilisateur vers le paiement via notre site pour une expérience de recherche et d'achat plus fluide.
Création de comptes Autoscope gratuits pour collecter des données sur les préférences des utilisateurs et ainsi améliorer notre offre.

# Projet réalisé par:
Gallouch Omar
Ghamlouche Mehdi
Nessah Hakim
