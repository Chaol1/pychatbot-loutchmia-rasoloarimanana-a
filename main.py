from functions import *
import time
if __name__ == '__main__':
    '''
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_names=surname(files_names)
    print(list_of_names)
    list_of_full_names=first_name(list_of_names)
    print(list_of_full_names)
    without=without_dubble(list_of_full_names)
    print(without)
    #convert_all_texts(files_names) (à ne plus exécuter)"""
    #convert_all_texts_2(files_names)
    '''
    dicTF=tf
    dicIDF=idf
    score_tf_idf=tf_idf(dicTF,dicIDF)
    print(score_tf_idf)

    unique=mots_uniques(corpus)
    scores=score_tf_idf
    files_names=list_of_files(corpus, "txt")
    TF_IDF=matrice_TfIdf(corpus,mots_uniques,scores,files_names)
    print(TF_IDF)
