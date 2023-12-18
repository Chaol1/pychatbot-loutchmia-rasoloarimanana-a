# common_words.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier common_words.py permet d'afficher la liste des mots qui sont à la fois dans la question et dans le corpus"""

from functions import * #De la branche token sur github

#Fonction 'common_words' qui permet d'afficher les mots communs
#Paramètres(corpus : Le répertoire avec tous les fihciers (cleaned notamment), question : Question posée par l'utilisateur)
#Résultat(common : Liste des mots communs)

def common_words(corpus, question):
    common=[]
    #Utiliser la fonction des mots uniques
    mots_corpus=mots_uniques(corpus)
    #Utiliser la fonction token
    mot=token(question)
    #Parcourir chaque terme
    for termes in mot:
        for mots in mots_corpus:
            if mots==termes and mots not in common:
                common.append(mots)
    return common
