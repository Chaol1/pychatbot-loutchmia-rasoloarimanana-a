# main.py ou main_first.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier main_first.py permet de tester toutes les fonctions utilisées dans la partie 1 avec un affichage plus clair pour se retrouver,
il ne s'agit pas encore du menu mais facilite la compréhenison du code."""

from functions import *
from functions_develop import *
if __name__ == '__main__':

    # Fonctions de base
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")

    list_of_names = surname(files_names)
    print("Liste des noms :", list_of_names)

    list_of_full_names = first_name(list_of_names)
    print("Liste des noms en entier :", list_of_full_names)

    without = without_dubble(list_of_full_names)
    print("Liste sans doublons :", without)

    #convert_all_texts(files_names) #(à n'exécuter qu'une seule fois)
    convert_all_texts_2(files_names)


    #Méthode TF-IDF
    corpus = "./cleaned"

    dic_TF=calcul_tf(corpus)
    print("Dic TF :",dic_TF)

    DocperWord = nbDocperWord(corpus)
    print("Dic du nombre de doc par mot :", DocperWord)

    dic_IDF=calcul_idf_final()
    print("Dic IDF :", dic_IDF)

    dic_scores=tf_idf(dic_TF,dic_IDF)
    print("Dic des Scores TF-IDF sous forme de matrice inversée :", dic_scores)

    unique = unique_words(corpus)
    print("Liste des mots uniques du corpus :", unique)

    TF_IDF=matrix_TfIdf(corpus,dic_scores,files_names)
    print("Matrice liste :", TF_IDF)

    dic_TF_IDF=matrixWithWords(corpus, dic_scores, files_names)
    print("Matrice dictionnaire avec mots :", dic_TF_IDF)

    #Fonctionnalités à développer

    less_imp=less_important(TF_IDF,unique)
    print("Liste des mots moins importants :", less_imp)

    max_score=high_score(TF_IDF,unique)
    print("Les mots au score TF-IDF le plus élevé :", max_score)

    chirac=words_Chirac(TF_IDF, unique)
    print("Chaîne des mots de Chirac :",chirac)

    nation=nation_analyse(dic_TF_IDF,list_of_names)
    print("Tuple présidents Nation et celui qui le dit le plus :",nation)

    climate=climate_names(dic_TF_IDF,list_of_names)
    print("Les présidents écologie/climat :", climate)
