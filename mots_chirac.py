# mots_chirac.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier mots_chirac.py permet d'afficher les mots les plus répétés par chirac dans ses 2 discours"""

#Fonction 'words_Chirac' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : liste des mots uniques)
#Utilisation de 'less_important' pour ne pas prendre en compte ces mots et de 'tf_chaine' pour calculer le tf des 2 documents sous forme de dictionnaire
#Résultat(words_chirac : Chaîne de caractères avec le(s) mot(s) le plus répété)


def words_Chirac(TF_IDF, unique):
    less_list = less_important(TF_IDF,unique)
    words_chirac = ""
    plus_word1 = 0
    plus_word2= 0
    #Ouvrir les 2 fichiers de Chirac
    with open("cleaned/Nomination_Chirac1.txt", "r", encoding="utf-8") as f1, open("cleaned/Nomination_Chirac2.txt", "r", encoding="utf-8") as f2:
        text1 = f1.read()
        text2 = f2.read()
    tf1 = tf_chaine(text1)
    tf2 = tf_chaine(text2)
    # Parcourir le premier fichier
    for word1, tf_doc1 in tf1.items():
        # Si le tf du mot est supérieur au tf de base et qu'il n'est pas dans la liste
        if tf_doc1 > plus_word1 and word1 not in less_list:
            plus_word1 = tf_doc1
            words_chirac = word1
    # Parcourir le deuxième fichier
    for word2, tf_doc2 in tf2.items():
        if tf_doc2 > plus_word2 and word2 not in less_list :
            plus_word2 = tf_doc2
            words_chirac = word2
    return words_chirac
