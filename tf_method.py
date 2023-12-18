# tf_method.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa,
Le fichier tf_method.py permet de calculer la fréquence de chaque mot dans chaque document (le score TF)"""


from functions import * #De la branche main.py


#La fonction 'tf_chaine' est générale, elle prend en paramètre une chaîne de caractères et permet de calculer le score TF de chaque mot."
#Création et retour d'un dictionnaire dans lequel les clés : mots, et les valeurs : scores TF des mots (occurence du mot dans la chaîne)"

def tf_chaine(text):
    dicOccurrence={}
    # Diviser la chaine en mots individuels
    words=text.split()
    # Parcourir chaque mot de la liste words
    for word in words:
        if word not in dicOccurrence :
            dicOccurrence[word]=1
        else:
            dicOccurrence[word]+=1
    return dicOccurrence


#La fonction 'calcul_tf' prend en paramètre le corpus et permet de calculer le score TF de chaque mot dans chaque fichier."
#Création et retour d'un dictionnaire de dictionnaires dans lequel les clés : les noms de fichiers et les valeurs : les dictionnaires comme dans la fonction précédente."

def calcul_tf(corpus):
    scores_tf = {}
    #Parcourir chaque fichier du répertoire
    for filename in os.listdir(corpus):
        #Ouvrir le fichier spécifié par le chemin complet en mode lecture
        with open(os.path.join(corpus, filename), "r",encoding="utf-8") as f:
            content = f.read()
            #Utiliser la fonction précédente pour chaque fichier
            dicOccurrence= tf_chaine(content)
            scores_tf[filename] = dicOccurrence
    return scores_tf

