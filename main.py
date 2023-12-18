from functions import *

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_names = surname(files_names)
    
    corpus = "./cleaned"
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)
    dic_mat = matrixWithWords(corpus, dic_scores, files_names)
    TF_IDF=
    nation=nation_analyse(dic_mat,list_of_names)
    chirac=words_Chirac(TF_IDF, unique)
    climat=climate_names(dic_TF_IDF,list_of_names)
    print("Les présidents écologie/climat :", climat)
