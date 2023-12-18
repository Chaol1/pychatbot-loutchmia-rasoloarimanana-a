from functions import *
from idf_method import *

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_names=surname(files_names)
    list_of_full_names=first_name(list_of_names)
    without=without_dubble(list_of_full_names)
    corpus = "./cleaned"
    dic_TF=calcul_tf(corpus)
    nbdocparmot = nbDocperWord(corpus)
    dic_IDF=calcul_idf_final()
    print("Dic IDF :", dic_IDF)
