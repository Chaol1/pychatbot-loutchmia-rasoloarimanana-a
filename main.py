from functions import *
from mots_chirac import *

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_names = surname(files_names)
    list_of_full_names = first_name(list_of_names)
    without = without_dubble(list_of_full_names)

    #Méthode TF-IDF
    corpus = "./cleaned"
    dic_TF=calcul_tf(corpus)
    nbdocparmot = nbDocperWord(corpus)
    dic_IDF=calcul_idf_final()
    dic_scores=tf_idf(dic_TF,dic_IDF)
    unique = unique_words(corpus)
    TF_IDF=matrix_TfIdf(corpus,dic_scores,files_names)
    dic_TF_IDF=matrixWithWords(corpus, dic_scores, files_names)
    
    #Fonctionnalités à développer

    moins_imp=less_important(TF_IDF,unique)
    chirac=words_Chirac(TF_IDF, unique)
    print("Chaîne des mots de Chirac :",chirac)
