# less_important.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier less_important.py permet d'afficher la liste des mots les moins importants dans le corpus"""

from matrix_tfidf import * #De la branche score_final sur github

#Fonction 'less_important' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : Liste des mots uniques)
#Résultat(words : Liste des mots les moins importants dans le corpus du document)

def less_important(TF_IDF,unique):
    words = []
    #j parcourt les mots uniques
    j = 0
    #Parcourir les vecteurs de la matrice
    for vector in TF_IDF:
        sum_vect = 0
        #Pour chaque valeur du vecteur
        for val in vector:
            sum_vect += val
        if sum_vect == 0.0:
            #Ajouter à la liste les mots correspondants
            words.append(unique[j])
        j += 1
    return words

