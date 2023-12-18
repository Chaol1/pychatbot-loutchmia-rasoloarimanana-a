from functions import *
from idf_method import *

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
    #convert_all_texts_2(files_names)'''
    
    directory = "./cleaned"
    dic_IDF=calcul_idf_final()
    print("Dic IDF :", dic_IDF)
