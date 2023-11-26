from functions import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    print(files_names)
    print(surname(files_names))
    list_of_names=surname(files_names)
    print(first_name(list_of_names))
    list_of_full_names=first_name(list_of_names)
    print(without_dubble(list_of_full_names))
    print(convert_all_texts(files_names))
    print(convert_all_texts_2(files_names))
    print(calculf_idf("./cleaned"))
    print(calcul_idf_final())