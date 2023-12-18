from functions import *

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    corpus = "./cleaned"

    dicTF = calcul_tf(corpus)
    print(dicTF)
    
    dicIDF = calcul_idf_final()
    print(dicIDF)
    
    dic_scores = tf_idf(dicTF, dicIDF)
    print(dic_scores)
    
    TF_IDF = matrix_TfIdf(corpus, dic_scores, files_names)
    print(TF_IDF)
    
    dic_mat = matrixWithWords(corpus, dic_scores, files_names)
    print(dic_mat)
