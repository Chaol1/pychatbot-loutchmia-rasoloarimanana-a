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
    corpus = "./cleaned"
    tf = calcul_tf(corpus)
    idf = calcul_idf_final()
    dicTF = tf
    dicIDF = idf
    scores=score_tf_idf
    files_names = list_of_files(corpus, "txt")
    print(ecologie_climat(corpus, mots_uniques, scores, files_names))
