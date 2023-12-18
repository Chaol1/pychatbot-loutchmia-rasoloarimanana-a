""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier similarite.py permet de mesurer la similarité entre deux textes représentés sous forme 
de vecteurs. Le fichier comporte trois fonctions produit_saclaire, norme et similarité qui permettent de calculer la similarité finale."""

from functions import * #De la branche token sur github

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

#Fonction générale 'general_similarity' qui calcule la similarité de deux vecteurs
#Paramètres(scalar_product,normA, normB : float qui sont retournés par les fonctions précédentes)
#Résultat(sim : float qui représente la similarité)

def general_similarity(scalar_product, normA, normB):
    sim = scalar_product / (normA*normB)
    return sim

#Fonction spécifique 'calcul_similarity' qui calcule cette fois la similarité entre chaque vecteur de la matrtice inversée et le vecteur de la question
#Paramètres(dic_scores: Matrice inversée sous forme de dictionnaire, vect_quest : Vecteur de la question sous forme de ditionnaire de dictionnaires)
#Utilisation de nos fonctions générales 'scalar_product', 'norm_vector', 'general_similarity' pour analyser chaque vecteur document avec le vecteur question
#Résultat(similarity : float qui représente la similarité)

def calcul_similarity(dic_scores, vect_quest):
    #Initialiser un dictionnaire pour chaque fonction
    scalarProduct = {}
    normQuestion = {}
    normDocs = {}
    similarity = {}
    #Parcourir la matrice TF-IDF
    for file, vector in dic_scores.items():
        #Pour chaque fonction générale, la stocker dans une variable pour chacun des N vecteurs (fichiers) de la matrice TF-IDF
        question = vect_quest[file]
        scalarProduct[file] = scalar_product(vector, question)
        normDocs[file] = norm_vector(vector)
        normQuestion[file] = norm_vector(question)
        #Fonction finale à afficher
        similarity[file] = general_similarity(scalarProduct[file], normDocs[file],normQuestion[file])
    return similarity
