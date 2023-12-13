import math

#Calcule le nombre d’occurrence de chaque mot dans une chaîne de caractère

def tf_chaine(texte):
    #Initialiser un dictionnaire
    dicOccurrence={}
    #Diviser la chaine en mots individuels
    mots=texte.split()
    #Parcourir chaque mot de la liste mots
    for mot in mots:
        #Si le mot n'est pas déjà dans le dictionnaire
        if mot not in dicOccurrence :
            #Initialiser à 1 l'occurence du mot
            dicOccurrence[mot]=1
        else:
            #Sinon incrémenter l'occurence de 1
            dicOccurrence[mot]+=1
    return dicOccurrence

#Calcul des scores TF pour chaque mot dans chaque fichier

def calcul_tf(corpus):
    scores_tf = {}
    #Parcourir chaque fichier du répertoire
    for filename in os.listdir(corpus):
        #Ouvrir le fichier spécifié par le chemin complet en mode lecture
        with open(os.path.join(corpus, filename), "r",encoding="utf-8") as f:
            contenu = f.read()
            #Utiliser la fonction précédente pour chaque fichier
            dicOccurrence= tf_chaine(contenu)
            #les clés du dictionnaire sont les noms du fichier
            #les valeurs sont les dictionnaires avec chaque mot et son score TF
            scores_tf[filename] = dicOccurrence
    return scores_tf
