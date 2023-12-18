# menu.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier menu.py est notre fichier principal. Il propose à l'utilisateur un menu avec 2 options.
La première est de choisir un chiffre entre 1 et 5 : chaque chifrre correspond à une fonctionnalité développée dans la partie 1.
La seconde lui permet de poser sa question et le chatBot luo répond en fonction des documents."""

from functions import *

import time

if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    list_of_names = surname(files_names)
    list_of_full_names = first_name(list_of_names)
    without = without_dubble(list_of_full_names)

    speeches = "./speeches"
    corpus_1 = speeches
    corpus = "./cleaned"

    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)
    TF_IDF = matrix_TfIdf(corpus, dic_scores, files_names)
    dic_mat = matrixWithWords(corpus, dic_scores, files_names)

    unique = unique_words(corpus)
    less_imp=less_important(TF_IDF,unique)
    score_max=high_score(TF_IDF,unique)
    chirac=words_Chirac(TF_IDF, unique)
    nation=nation_analyse(dic_mat,list_of_names)
    climate=climate_names(dic_mat,list_of_names)



    print('Bonjour cher utilisateur ! Entrez le numéro de votre choix entre 1 et 5 ou posez directement une question')
    print()
    print('Première option : MENU ')
    print('1. Les mots les moins importants dans le corpus')
    print('2. Les mots les plus importants')
    print('3. Les mots les plus répétés par M.Chirac ')
    print('4. Le président qui repète le plus le mot "Nation" ')
    print('5. Les présidents qui ont parlés du climat ou de l écologie ')
    print()
    time.sleep(0.5)
    print('Deuxième option : Mode Chatbot (posez une question libre) ')
    time.sleep(0.5)
    print()

    while True :
        choix = input("Votre choix : ")
        if choix == '1':
            print('A votre service ! Voici les mots les moins importants :', less_imp)
            print()
            time.sleep(1.5)
        elif choix == '2':
            print('Biensûr ! Les mots les plus importants sont :', score_max)
            print()
            time.sleep(1.5)
        elif choix == '3':
            print('M.Chirac a dit le plus souvent le ou les mots suivant(s) :', chirac)
            print()
            time.sleep(1.5)
        elif choix == '4':
            print('Voici les présidents ayant évoqués le mot "Nation" ainsi que celui qui l a répété le plus:', nation)
            print()
            time.sleep(1.5)
        elif choix == '5':
            print('Les présidents qui ont parlé du climat ou de l écologie sont :', climate)
            print()
            time.sleep(1.5)
        elif not choix:
            next
        else:
            question = choix
            vecteur_quest = quest_tf_idf(question, corpus)
            doc_pert = doc_plus_pert(question, corpus)
            maxi_mot = maxi_tfidf(vecteur_quest)
            sentence = sentence_word(corpus_1, doc_pert, maxi_mot)
            answer_final = answer_chatbot(question, sentence)
            print(answer_final)
            time.sleep(2)

        #break si l'on ne veut plus exécuter le code
