#Fonction générale 'norm_vector' qui calcule la norme d'un vecteur
#Paramètres(vect : Un vecteur sous forme d'un dictionnaire où clés : mots et valeurs : score tf-idf)
#Résultat(norm : float qui est la norme)

from math import *

def norm_vector(vect):
    s = 0.0
    for word, score in vect.items():
        s+= score**2
    norm=sqrt(s)
    #Si la norme est égale à 0 alors norme prend 1 (pour ne pass diviser par 0)
    if norm == 0.0:
        norm = 1.0
    return norm
