# idf_method.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier idf_method.py permet de calculer la fréquence inverse du document pour chaque mot dans chaque document (le score IDF)"""

from functions import *   #De la branche main sur github
from tf_method import *  #De la branche tf sur github
import math


#Fonction 'nbWordperDoc' prend en paramètre le corpus 'cleaned' et permet de calculer le nombre de documents contenat le mot."
#Création et retour d'un dictionnaire dans lequel les clés : mots, et les valeurs : nombre de documents en tant que float"

def nbDocperWord(corpus):
    dico={}
    files_names=list_of_files(corpus, "txt")
    content_file = []
    #Parcourir chaque nom de fichier
    for file in files_names:
        #Avoir le chemin complet du fichier avec le corpus
        path1=os.path.join("./cleaned", file)
        with open(path1, "r",encoding="utf-8") as f1:
            content=f1.read()
            words=content.split()
        #Parcourir chaque élément de la liste "mots"
        for elt in words:
            if elt in dico and elt not in content_file:
                dico[elt] += 1.0
                content_file.append(elt)
            elif (elt not in dico):
                dico[elt] = 1.0
                content_file.append(elt)
        #Réinitialiser de la liste pour chaque changement de fichier
        content_file = []
    return dico


#Fonction 'calcul_idf_final' permet de calculer le score IDF (la fréquence inverse) de chaque mot dans chaque document du courpus
#Ne prend pas de patramètres mais utilise la fonction 'nbDocperWord' et 'list_of_files' directement dans le corps de la fonction
#dico : Dictionnaire pour avoir le nombre de document par mot
#files : Liste pour avoir les noms des fichiers
#Résultat (dico : Dictionnaire modifié avec comme clés : les mots et valeurs : les scores IDF)

def calcul_idf_final():
    dico=nbDocperWord("./cleaned")
    #Récupérer la liste des fichiers du répertoire
    files=list_of_files("./cleaned", "txt")
    for file,nb in dico.items():
        #Calcul du logarithme de la proportion inversée et arrondir à 4 chiffres après la virgule
        dico[file]=round(math.log10(len(files)/nb),4)
    return dico
