"""My first chatbot - Laïli LOUTCHMIA & Malalasoa RASOLOARIMANANA
Fonction retournant les mots ayant un score TF-IDF le plus élevé."""

# Score TF-IDF le plus élevé
#Paramètres(TF_IDF:Matrice TF-IDF, unique: Liste des mots sans doublons.)
#(words:chaîne de caractères comportant tous les mots au score TF-IDF le plus élevé)
def score_eleve(TF_IDF,unique):
    words = " "
    #j parcourt les mots uniques
    j = 0
    maxi = 0.0
    #Parcourir les vecteurs de la matrice
    for vector in TF_IDF:
        sum_vector = 0
        #Pour chaque valeur du vecteur
        for val in vector:
            #Ajouter la valeur à la somme
            sum_vector += val
        if sum_vector > maxi:
            maxi=sum_vector
            words+= unique[j] + " "
        j += 1
    return words
