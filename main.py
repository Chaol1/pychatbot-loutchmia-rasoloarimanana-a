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
    directory = "./cleaned"
    '''
    directory = "./cleaned"

    #corriger pour avoir tous les docs
    corpus= get_texts_from_documents(directory)#tous les textes
    textsNames = list_of_files(directory,'txt')#tous les noms

    dicTF = {}
    i = 0
    for texte in corpus:
        dicTF[textsNames[i]]  = calcul_tf(texte)#TF
        i+=1

    listOfWordsDeduplicated, wordsPerDoc = nbDocsPerWord(corpus)
    dicIDF = inverse_proportion(wordsPerDoc,len(corpus))

    scores = makeScore(dicTF,dicIDF)
    matrixTfIdf = makeMatrixTfIdf(listOfWordsDeduplicated,scores,textsNames)

    leastTfIdfWords = orderVectorAsc(matrixTfIdf,listOfWordsDeduplicated)
    mostTfIdfWords = orderVectorDesc(matrixTfIdf,listOfWordsDeduplicated)
    chirac = chiracAnalysis(corpus)
    nation = nationAnalysis(corpus)
    ecologie = ecologieAnalysis(corpus)
    commonWords = allCommonWords(listOfWordsDeduplicated,corpus)

    while True:
        print('Menu :')
        print('1. Les mots les moins importants dans le corpus')
        print('2. Les mots les plus importants')
        print('3. Les mots les plus répétés par M.Chirac ')
        print('4. Le président qui repète le plus le mot "Nation" ')
        print('5. Le premier président à parler du climat ou de l écologie ')
        print('6. Les mots communs à tous les discours')

        choice = input('Entrez le numéro de votre choix : ')
        if choice == '1':
            print('Les mots les moins importants sont :',leastTfIdfWords)
            time.sleep(2)
        elif choice == '2':
            print('Les mots les plus importants sont :',mostTfIdfWords)
            time.sleep(2)
        elif choice == '3':
            print('Le(s) mot(s) le(s) plus répété(s) par M.Chirac sont :',chirac)
            time.sleep(2)
        elif choice == '4':
            print('Le président qui repète le plus le mot "Nation" est :',nation)
            time.sleep(2)
        elif choice == '5':
            print('Le premier président à parler du climat ou de l écologie est :',ecologie)
            time.sleep(2)
        elif choice == '6':
            print('Les mots communs à tous les discours sont :',commonWords)
            time.sleep(2)
