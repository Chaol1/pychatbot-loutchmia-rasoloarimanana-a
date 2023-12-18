from functions import *
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    corpus = "./cleaned"
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)
    TF_IDF = matrice_TfIdf(corpus, dic_scores, files_names)
    unique = unique_words(corpus)
    score_max=score_eleve(TF_IDF,unique)
