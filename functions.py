# Liste des mots les moins importants
def not_important(matrice, mots_uniques):
    mots = []
    #j parcourt les mots uniques
    j = 0
    #Parcourir les vecteurs de la matrice
    for vecteur in matrice:
        #Initialiser la somme à 0
        somme_vecteur = 0
        #Pour chaque valeur du vecteur
        for valeur in vecteur:
            #Ajouter la valeur à la somme
            somme_vecteur += valeur
        #Si la somme est nulle
        if somme_vecteur == 0.0:
            #Ajouter à la liste les mots correspondants
            mots.append(mots_uniques[j])
        j += 1
    return mots
