# climat_ecologie.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier climat_ecologie.py permet d'indiquer les noms des présidents qui ont parlé du climat en général"""

from matrix_tfidf import * #De la branche score_final sur github

#Fonction 'climate_words' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : liste des mots uniques)
#Utilisation de 'less_important' pour ne pas prendre en compte ces mots et de 'tf_chaine' pour calculer le tf des 2 documents sous forme de dictionnaire
#Résultat(words_chirac : Chaîne de caractères avec le(s) mot(s) le plus répété)

def climate_names(dic_TF_IDF,list_of_names):
    names=""
    #Parcourir la matrice avec les mots
    for word,vect in dic_TF_IDF.items():
        if word=='écologie' or word=='climat' or word=='climatique' or word=='écologique':
            #Parcourir les listes vecteurs
            for i in range (len(vect)):
                for j in range (len(list_of_names)):
                    #Si la valeur est différente de 0 et à la même position que le nom
                    if vect[i]!=0.0 and i==j and list_of_names[j] not in names :
                        names += list_of_names[j] + " "
    return names
