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
    words_corpus=unique_words(corpus)
    #Utiliser la fonction token
    word=token(question)
    #Parcourir chaque terme
    for terms in word:
        for words in words_corpus:
            if words==terms and words not in common:
                common.append(mots)
    return common
