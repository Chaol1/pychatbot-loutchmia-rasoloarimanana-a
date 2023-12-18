from functions import *
from tf_method import *

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_full_names=first_name(list_of_names)
    without=without_dubble(list_of_full_names)
    
    corpus = "./cleaned"
    dic_TF=calcul_tf(corpus)
    print("Dic TF :",dic_TF)
