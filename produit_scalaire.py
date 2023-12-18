#Fonction générale 'scalar_product' qui calcule le produit scalaire entre 2 vecteurs
#Paramètres(vectA, vectB : Deux vecteurs sous forme de dictionnaire où clés : mots et valeurs : score tf-idf)
#Résultat(scalar : float qui est le produit scalaire)


def scalar_product(vectA,vectB):
    scalar = 0
    #Parcourir le vecteur A
    for wordA,scoreA in vectA.items():
        #Parcourir le vecteur B
        for wordB, scoreB in vectB.items():
            #Si le mot est le même dans les deux vecteurs
            if wordA == wordB:
                #Faire la somme des produits des scores tfidf du mot dans les deux vecteurs
                scalar += scoreA * scoreB
    return scalar

