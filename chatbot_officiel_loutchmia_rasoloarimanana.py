"""My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Toutes les fonctions du chatbot dans un seul fichier"""

import os
import math

# Fonction qui parcourt la liste des fichiers d’une extension donnée, dans un répertoire donné
# Paramètres(directory: Chemin du répertoire "speeches", extension: extension des fichiers issus de "speeches", ici "txt")
# Résultat(files_names: Liste des noms des fichiers textes contenus dans le répertoire "speeches")

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


# Extraire les noms des présidents à partir des noms des fichiers texte fournis
# Paramètre(files_names: Liste des noms des fichiers texte de "speeches")
# Résultat(list_of_names: Liste des noms de famille des présidents)

def surname(files_names):
    list_of_names = []
    # Initialiser une chaîne vide
    chain = ""
    # Parcourir la liste des noms de fichier
    for i in range(len(files_names)):
        # Réinitialiser la chaine pour stocker le nom à chaque début de la boucle
        chain = ""
        for j in range(len(files_names[i])):
            # A partir de la 1ère lettre du nom (j>=11)
            if j >= 11 and j < len(files_names[i]) - 4 and files_names[i][j] != "1" and files_names[i][j] != "2":
                # Ajouter le caractère à la chaine
                chain += (files_names[i][j])
        # Ajouter le nom à la liste des noms
        list_of_names.append(chain)
    return (list_of_names)


# Associer à chaque président son prénom
# Paramètre(list_of_names: Liste des noms de famille des présidents)
# Résultat(list_of_full_names: Liste des noms et prénoms présidentiels)

def first_name(list_of_names):
    # Initialiser en dur la liste des prénoms
    list_of_first_names = ["Jacques ", "Jacques ", "Valéry ", "François ", "Emmanuel ", "François ", "François ",
                           "Nicolas "]
    list_of_full_names = []
    for i in range(len(list_of_names)):
        # Ajouter à la liste des noms complets la combinaison des prénoms + noms de la liste à la même position
        list_of_full_names.append(list_of_first_names[i] + list_of_names[i])
    return (list_of_full_names)


# Afficher la liste des noms des présidents sans doublons
# Paramètre(list_of_full_names:Liste des noms complets des présidents)
# Résultat(without: Liste des noms et prénoms présidentiels sans doublons)

def without_dubble(list_of_full_names):
    without = []
    for i in range(len(list_of_full_names)):
        # Si le nom n’est pas déjà dans la liste vide
        if list_of_full_names[i] not in without:
            # Ajouter ce nom à liste
            without.append(list_of_full_names[i])
    return without


# Convertir les textes des 8 fichiers en minuscules + création du répertoire cleaned
# Paramètre(files_names: Liste des fichiers texte de "speeches")
# Résultat(Pas de résultat retourné mais les fichiers texte ont été copiés dans le répertoire "cleaned" et y ont été modifiés)

def convert_all_texts(files_names):
    # Créer le répertoire "cleaned"
    os.mkdir("cleaned")
    line2 = ""
    # Parcourir les fichiers un à un
    for file in files_names:
        # Créer un chemin vers chaque fichier avec son répertoire
        path1 = os.path.join("./speeches", file)
        path2 = os.path.join("./cleaned", file)
        # Ouvrir les deux fichiers en même temps
        with open(path1, "r") as f1, open(path2, "w") as f2:
            # Pour chaque ligne du fichier ouvert de f1
            for line in f1:
                line2 = ""
                # Pour chaque caractère de la ligne
                for i in range(len(line)):
                    # Si le code ASCII du caractère est dans l’intervalle des majuscules
                    if (ord(line[i])) >= 65 and (ord(line[i])) <= 90:
                        # Ajouter à la chaîne le caractère converti en minuscule
                        line2 += chr(ord(line[i]) + 32)
                    else:
                        # Ajouter le caractère si ce n’est pas une majuscule
                        line2 += line[i]
                f2.write(line2)


# Supprimer tous les caractères de ponctuation dans les fichiers de cleaned
# Paramètre(files_names: Liste des noms des fichiers texte partagés de "speeches" et "cleaned")
# Résultat(Pas de résultat retourné mais les fichiers de "cleaned" ont été modifiés.)

def convert_all_texts_2(files_names):
    line1 = ""
    # Parcourir chaque fichier
    for file in files_names:
        txt = ""
        # Créer un chemin en joignant le répertoire cleaned avec le fichier
        path1 = os.path.join("./cleaned", file)
        with open(path1, 'r') as f1:
            content = f1.readlines()
            # Parcourir chaque ligne du contenu du fichier
            for line in content:
                # Parcourir chaque caractère de chaque ligne
                for i in range(len(line)):
                    # Ajouter un espace à la chaîne de caractères si apostrophe ou tiret
                    if (line[i] == "'" or line[i] == "-"):
                        line1 += " "
                    # Si le caractère n’est pas un caractère de ponctuation
                    elif line[i] != "," and line[i] != "." and line[i] != ";" and line[i] != "?" and line[i] != "!" and \
                            line[i] != ";" and line[i] != '"' and line[i] != ':':
                        line1 += line[i]
                txt += line1
                # Réinitialiser la chaîne ligne à une chaîne vide
                line1 = ""
        f = open(path1, 'w')
        # Ecrire le contenu modifié dans le fichier
        f.write(txt)
        f.close()

#La fonction 'tf_chaine' est générale, elle prend en paramètre une chaîne de caractères et permet de calculer le score TF de chaque mot."
#Création et retour d'un dictionnaire dans lequel les clés : mots, et les valeurs : scores TF des mots (occurence du mot dans la chaîne)"

def tf_chaine(text):
    dicOccurrence={}
    # Diviser la chaine en mots individuels
    words=text.split()
    # Parcourir chaque mot de la liste words
    for word in words:
        if word not in dicOccurrence :
            dicOccurrence[word]=1
        else:
            dicOccurrence[word]+=1
    return dicOccurrence


#La fonction 'calcul_tf' prend en paramètre le corpus et permet de calculer le score TF de chaque mot dans chaque fichier."
#Création et retour d'un dictionnaire de dictionnaires dans lequel les clés : les noms de fichiers et les valeurs : les dictionnaires comme dans la fonction précédente."

def calcul_tf(corpus):
    scores_tf = {}
    #Parcourir chaque fichier du répertoire
    for filename in os.listdir(corpus):
        #Ouvrir le fichier spécifié par le chemin complet en mode lecture
        with open(os.path.join(corpus, filename), "r",encoding="utf-8") as f:
            content = f.read()
            #Utiliser la fonction précédente pour chaque fichier
            dicOccurrence= tf_chaine(content)
            scores_tf[filename] = dicOccurrence
    return scores_tf


#Fonction 'nbWordperDoc' prend en paramètre le corpus 'cleaned' et permet de calculer le nombre de documents contenat le mot."
#Création et retour d'un dictionnaire dans lequel les clés : mots, et les valeurs : nombre de documents en tant que float"

def nbDocperWord(corpus):
    dico={}
    files_names=list_of_files(corpus, "txt")
    content_file = []
    #Parcourir chaque nom de fichier
    for file in files_names:
        #Avoir le chemin complet du fichier avec le corpus
        path1=os.path.join("./cleaned", file)
        with open(path1, "r",encoding="utf-8") as f1:
            content=f1.read()
            words=content.split()
        #Parcourir chaque élément de la liste "mots"
        for elt in words:
            if elt in dico and elt not in content_file:
                dico[elt] += 1.0
                content_file.append(elt)
            elif (elt not in dico):
                dico[elt] = 1.0
                content_file.append(elt)
        #Réinitialiser de la liste pour chaque changement de fichier
        content_file = []
    return dico


#Fonction 'calcul_idf_final' permet de calculer le score IDF (la fréquence inverse) de chaque mot dans chaque document du courpus
#Ne prend pas de patramètres mais utilise la fonction 'nbDocperWord' et 'list_of_files' directement dans le corps de la fonction
#dico : Dictionnaire pour avoir le nombre de document par mot
#files : Liste pour avoir les noms des fichiers
#Résultat (dico : Dictionnaire modifié avec comme clés : les mots et valeurs : les scores IDF)

def calcul_idf_final():
    dico=nbDocperWord("./cleaned")
    #Récupérer la liste des fichiers du répertoire
    files=list_of_files("./cleaned", "txt")
    for file,nb in dico.items():
        #Calcul du logarithme de la proportion inversée et arrondir à 4 chiffres après la virgule
        dico[file]=round(math.log10(len(files)/nb),4)
    return dico

#Calcul du score TF-IDF

def tf_idf(dic_TF,dic_IDF):
    scores = {}
    #Parcourir le dictionnaire TF
    for file,dicOcc in dic_TF.items():
        #Initialiser un  dictionnaire vide comme valeur
        scores[file] = {}
        #Parcourir le dictionnaire valeur du dicTF
        for mot,tf in dicOcc.items():
            #Calcul du score TF-IDF pour chaque mot
            scores[file][mot] = tf * dic_IDF[mot]
    return scores

def unique_words(corpus):
    list_of_words = []
    files_names = list_of_files(corpus, "txt")
    #Parcourir chaque fichier de la liste
    for file in files_names:
        path1 = os.path.join("./cleaned", file)
        with open(path1, "r", encoding="utf-8") as f1:
            content = f1.read()
            words = content.split()
        #Pour chaque mot
        for word in words:
            #Ajouter tous les mots de tous les fichiers
            list_of_words.append(word)
    #Initialiser une liste vide
    unique = []
    #Pour chaque mot de la liste de tous les mots
    for word in list_of_words:
        #Si le mot n'est pas dans la liste de mots unique
        if word not in unique:
            #Ajouter le mot
            unique.append(word)
    return unique

#Création de la matrice TF-IDF

def matrix_TfIdf(corpus,scores,files_names):
    M = []
    #Utiliser la fonction précédente pour avoir les mots uniques
    list_of_words=unique_words(corpus)
    #Pour chaque mot de la liste
    for word in list_of_words:
        #Initialiser une liste vecteur numérique
        vector_num= []
        #Parcourir chaque fichier
        for file in files_names:
            #Si le mot est dans le dic des scores TF-IDF
            if word in scores[file]:
                #Ajouter à son vecteur de scores le vecteur numérique
                vector_num.append(scores[file][word])
            else:
                #Sinon ajouter un score de 0
                vector_num.append(0.0)
        #Ajouter à la matrice le vecteur de scores pour chaque mot
        M.append(vector_num)
    return M


#Fonction 'matrixWithWord' que nous avons ajouter afin de rendre l'affichage plus compréhensible pour associer chaque mot avec son vecteur de scores
#Retourne un dictionnaire avec comme clés : les mots et comme valeurs : les vecteurs sous forme de liste

def matrixWithWords(corpus, dic_scores, files_names):
    M = {}
    # Utiliser la fonction précédente pour avoir les mots uniques
    list_words = unique_words(corpus)
    # Pour chaque mot de la liste
    for word in list_words:
        # Initialiser une liste vecteur numérique
        vect_num = []
        # Parcourir chaque fichier
        for file in files_names:
            # Si le mot est dans le dic des scores TF-IDF
            if word in dic_scores[file]:
                # Ajouter à son vecteur de scores le vecteur numérique
                vect_num.append(dic_scores[file][word])
            else:
                # Sinon ajouter un score de 0
                vect_num.append(0.0)
        # Ajouter à la matrice le vecteur de scores pour chaque mot
        M[word] = vect_num
    return M

#Fonction 'less_important' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : liste des mots uniques)
#Résultat(words : Liste des mots les moins importants dans le corpus du document)
def less_important(TF_IDF,unique):
    words = []
    #j parcourt les mots uniques
    j = 0
    #Parcourir les vecteurs de la matrice
    for vector in TF_IDF:
        sum_vect = 0
        #Pour chaque valeur du vecteur
        for val in vector:
            sum_vect += val
        if sum_vect == 0.0:
            #Ajouter à la liste les mots correspondants
            words.append(unique[j])
        j += 1
    return words

# Score TF-IDF le plus élevé
#Paramètres(TF_IDF:Matrice TF-IDF, unique: Liste des mots sans doublons.)
#(words:chaîne de caractères comportant tous les mots au score TF-IDF le plus élevé)

def high_score(TF_IDF,unique):
    words = " "
    #j parcourt les mots uniques
    j = 0
    maxi = 0.0
    #Parcourir les vecteurs de la matrice
    for vector in TF_IDF:
        sum_vector = 0
        #Pour chaque valeur du vecteur
        for val in vector:
            #Ajouter la valeur à la somme
            sum_vector += val
        if sum_vector > maxi:
            maxi=sum_vector
            words+= unique[j] + " "
        j += 1
    return words

# mots_chirac.py

#Fonction 'words_Chirac' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : liste des mots uniques)
#Utilisation de 'less_important' pour ne pas prendre en compte ces mots et de 'tf_chaine' pour calculer le tf des 2 documents sous forme de dictionnaire
#Résultat(words_chirac : Chaîne de caractères avec le(s) mot(s) le plus répété)

def words_Chirac(TF_IDF, unique):
    less_list = less_important(TF_IDF,unique)
    words_chirac = ""
    plus_word1 = 0
    plus_word2= 0
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


# Liste des présidents ayant parlé de la "nation" et celui qui en a le plus parlé
#Paramètres(dic_mat:Matrice TF-IDF dont les clés sont les mots et les valeurs, leur score TF-IDF, list_of_names: Liste des noms des présidents)
#Résultat(noms: chaîne de caractères contenant les noms des présidents parlant de "nation" plus: nom du président qui la mentionne le plus.)

def nation_analyse(dic_mat,list_of_names):
    noms=""
    plus_rep=0.0
    #Parcourir la matrice avec les mots
    for mot,vecteur in dic_mat.items():
        if mot=='nation':
            #Parcourir les valeurs du vecteur du mot nation
            for i in range (len(vecteur)):
                #Parcourir la liste des mots moins importants
                for j in range (len(list_of_names)):
                    #Si la valeur est différente de 0 et le mot n'est pas dans la liste
                    if vecteur[i]!=0.0 and i==j and list_of_names[j] not in noms :
                        noms += list_of_names[j] + " "
                        #Chercher le max
                        if vecteur[i]>plus_rep:
                            plus_rep=vecteur[i]
                            plus=list_of_names[j]
    return noms,plus



# climat_ecologie.py

#Fonction 'climate_words' qui permet d'afficher les mots avec un score TF-IDF nul donc les mots les moins importants
#Paramètres(TF_IDF : Matrice TF_IDF sous forme de liste, unique : liste des mots uniques)
#Utilisation de 'less_important' pour ne pas prendre en compte ces mots et de 'tf_chaine' pour calculer le tf des 2 documents sous forme de dictionnaire
#Résultat(words_chirac : Chaîne de caractères avec le(s) mot(s) le plus répété)

def climate_names(dic_TF_IDF,list_of_names):
    names=""
    #Parcourir la matrice avec les mots
    for word,vect in dic_TF_IDF.items():
        if word=='écologie' or word=='climat' or word=='climatique' or word=='écologique':
            #Parcourir les listes vecteurs
            for i in range (len(vect)):
                for j in range (len(list_of_names)):
                    #Si la valeur est différente de 0 et à la même position que le nom
                    if vect[i]!=0.0 and i==j and list_of_names[j] not in names :
                        names += list_of_names[j] + " "
    return names

#Fonction qui "tokenise" les termes d'une question, c'est-à-dire que chaque mot de la question est séparé dans une liste et perd sa majuscule s'il en a
#Paramètre(question: question sous forme de chaîne de caractères)
#Résultat(words: Liste des mots de la question tokenisés)

def token(question):
    words=[]
    ch=""
    for i in range(len(question)): #Parcours de la question en tant que chaîne de caractères
        #Si le carcatère est dans l'intervalle des majuscules
        if ord(question[i])>=65 and ord(question[i])<=90:
            ch+=chr(ord(question[i])+32)
        #Si le caractère est un signe de ponctuation
        elif question[i]!="," and question[i]!="." and question[i]!=";" and question[i]!="?" and question[i]!="!" and question[i]!=";" and question[i]!='"'and question[i]!=':' and question[i]!=" " and question[i]!="-" and question[i]!="'":
            ch+=question[i]
        else:
            if ch!="":
                words.append(ch) #ajout du mot tokenisé dans la liste
            ch=""
    return words

#Modification de la fonction tf de base, initialisation de toutes les valeurs à 0.0
#Paramètre(text: Ici corpus, correspond au chemin du répertoire "cleaned".)
#Résultat(dicOccurence: Dictionnaire où chaque TF des mots est initialisé à 0.0)

def tf_chain_bis(text):
    #Initialiser un dictionnaire
    dicOccurrence={}
    #Diviser la chaine en mots individuels
    words=text.split()
    #Parcourir chaque mot de la liste mots
    for word in words:
        #Si le mot n'est pas déjà dans le dictionnaire
        if word not in dicOccurrence :
            #Initialiser l'occurence du mot
            dicOccurrence[word]=0.0
    return dicOccurrence


#Calcul des scores TF avec la matrice TF modifiée
#Paramètre(corpus: chemin du répertoire "cleaned")
#Résultat(Dictionnaire de dictionnaires dont la clé correspond au nom du document et sa valeur au dictionnaire TF de chaque document)

def calcul_tf_bis(corpus):
    scores_tf = {}
    #Parcourir chaque fichier du répertoire
    for filename in os.listdir(corpus):
        #Ouvrir le fichier spécifié par le chemin complet en mode lecture
        with open(os.path.join(corpus, filename), "r",encoding="utf-8") as f:
            content = f.read()
            #Utiliser la fonction précédente pour chaque fichier
            dicOccurrence= tf_chain_bis(content)
            #les clés du dictionnaire sont les noms du fichier
            #les valeurs sont les dictionnaires avec chaque mot et son score TF
            scores_tf[filename] = dicOccurrence
    return scores_tf

#Création d'un dictionnaire qui a cette fois-ci les scores TF des termes de la question
#Paramètres(question: question sous forme de chaîne de caractères, corpus: chemin du répertoire "cleaned")
#Résultat(mat: Dictionnaire de dictionnaires, clé qui correspond au nom du document et valeur, au dictionnaire des scores TF des mots des fichiers et ceux de la question)

def quest_final(question, corpus):
    quest=token(question)
    mat=calcul_tf_bis(corpus)
    for elt in quest: #Parcours des termes de la question
        for doc in mat.keys(): #Parcours des différents fichiers texte
            if elt in mat[doc].keys(): #Si terme de la question est dans les clés du sous-dictionnaire de mat
                mat[doc][elt]+=1
    return mat

#Matrice finale TF-IDF de la question
#Paramètres(question: question sous forme de chaîne de caractères, corpus: chemin du répertoire "cleaned")
#Résultat(mat_tf_idf: Dictionnaire de dictionnaires, clé qui correspond au nom du document et valeur, au dictionnaire des scores TF-IDF des mots des fichiers et ceux de la question)

def quest_tf_idf(question, corpus):
    quest=token(question)
    mat_tf_idf=quest_final(question, corpus) #Matrice qu'avec les scores TF
    mat_idf=calcul_idf_final() #Matrice IDF
    for elt in quest:
        for doc in mat_tf_idf.keys():
            for elt in mat_tf_idf[doc].keys():
                mat_tf_idf[doc][elt]= mat_tf_idf[doc][elt]*mat_idf[elt] #Multiplication des scores TF et IDF
    return mat_tf_idf

#Fonction générale 'scalar_product' qui calcule le produit scalaire entre 2 vecteurs
#Paramètres(vectA, vectB : Deux vecteurs sous forme de dictionnaire où clés : mots et valeurs : score tf-idf)
#Résultat(scalar : float qui est le produit scalaire)


def scalar_product(vectA,vectB):
    scalar = 0
    #Parcourir le vecteur A
    for wordA,scoreA in vectA.items():
        #Parcourir le vecteur B
        for wordB, scoreB in vectB.items():
            #Si le mot est le même dans les deux vecteurs
            if wordA == wordB:
                #Faire la somme des produits des scores tfidf du mot dans les deux vecteurs
                scalar += scoreA * scoreB
    return scalar

#Fonction générale 'norm_vector' qui calcule la norme d'un vecteur
#Paramètres(vect : Un vecteur sous forme d'un dictionnaire où clés : mots et valeurs : score tf-idf)
#Résultat(norm : float qui est la norme)

from math import *

def norm_vector(vect):
    s = 0.0
    for word, score in vect.items():
        s+= score**2
    norm=sqrt(s)
    #Si la norme est égale à 0 alors norme prend 1 (pour ne pass diviser par 0)
    if norm == 0.0:
        norm = 1.0
    return norm

#Fonction générale 'general_similarity' qui calcule la similarité de deux vecteurs
#Paramètres(scalar_product,normA, normB : float qui sont retournés par les fonctions précédentes)
#Résultat(sim : float qui représente la similarité)

def general_similarity(scalar_product, normA, normB):
    sim = scalar_product / (normA*normB)
    return sim

#Fonction spécifique 'calcul_similarity' qui calcule cette fois la similarité entre chaque vecteur de la matrtice inversée et le vecteur de la question
#Paramètres(dic_scores: Matrice inversée sous forme de dictionnaire, vect_quest : Vecteur de la question sous forme de ditionnaire de dictionnaires)
#Utilisation de nos fonctions générales 'scalar_product', 'norm_vector', 'general_similarity' pour analyser chaque vecteur document avec le vecteur question
#Résultat(similarity : float qui représente la similarité)

def calcul_similarity(dic_scores, vect_quest):
    #Initialiser un dictionnaire pour chaque fonction
    scalarProduct = {}
    normQuestion = {}
    normDocs = {}
    similarity = {}
    #Parcourir la matrice TF-IDF
    for file, vector in dic_scores.items():
        #Pour chaque fonction générale, la stocker dans une variable pour chacun des N vecteurs (fichiers) de la matrice TF-IDF
        question = vect_quest[file]
        scalarProduct[file] = scalar_product(vector, question)
        normDocs[file] = norm_vector(vector)
        normQuestion[file] = norm_vector(question)
        #Fonction finale à afficher
        similarity[file] = general_similarity(scalarProduct[file], normDocs[file],normQuestion[file])
    return similarity

#Fonction qui retourne le fichier qui a la similarité la plus proche du vecteur de la question
#Paramètres(question: question sous forme de chaîne de caractères, corpus: chemin du répertoire "cleaned")
#Résultat(doc_pert: Nom du fichier qui a la similarité la plus proche du vecteur de la question)

def doc_plus_pert(question, corpus):
    #Utilisation du vecteur de la question
    vect_quest=quest_tf_idf(question, corpus)
    #Utilisation de la matrice TF-IDF
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)
    #Utilisation de la fonction similarité
    similarity = calcul_similarity(dic_scores, vect_quest)
    maxi_sim = 0
    for file, value in similarity.items(): #Parcours du dictionnaire
        if value > maxi_sim: #value a la similarité la plus élevée
            doc_pert = file #récupération du fichier à la similarité la plus élevée
            maxi_sim = value
    return doc_pert

#Fonction 'maxi_tfidf' qui retourne le mot
#Paramètres(vect_quest : Vecteur de la question sous forme de dictionnaire de dictionnaires)
#Résultat(word_max : mot de la question avec le max tf-df)

def maxi_tfidf(vect_quest):
    maxi = 0.0
    #Parcourir le vecteur de la question
    for file, vector in vect_quest.items():
        for word,score in vector.items():
            #Chercher le score max et le mot qui lui correspond
            if vector[word] > maxi:
                maxi=vector[word]
                word_max=word
    return word_max

#Fonction 'sentence_word' qui prend en paramètres :
#(corpus : le répertoire de documents, document :le document le plus pertinent, maxi_word : le mot avec les max score)
#Paramètres(vect_quest : Vecteur de la question sous forme de dictionnaire de dictionnaires)
#Résultat(phrase : première phrase avec le mot max de la question)
def sentence_word(corpus, document, maxi_word):
    #Ouvrir le document le plus pertinent
    with open(os.path.join(corpus, document), "r", encoding="utf-8") as f:
        contenu = f.read()
        #Diviser le contenu en phrases avec un point
        phrases = contenu.split('.')
        #Parcourir chaque phrase de la liste de phrases
        for phrase in phrases:
            if maxi_word in phrase:
                return phrase

#Fonction qui améliore les réponses apportées par le chatbot
#Paramètres(question: question sous forme de chaîne de caractères, phrase: réponse précédente sous forme de chaîne de caractères)
#Résultat(phrase: Réponse améliorée)

def answer_chatbot(question,sentence):
    #Dictionnaire avec le début des questions
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!",
        "Quel": "Le voici, ",
        "Quels": "Ce sont, ",
        "Quand": "La date est, "
    }
    answer = sentence
    for word_question, answer_beginning in question_starters.items(): #Parcours du dictionnaire question_starters
        if question.split()[0] == word_question: #Si le premier terme de la question correspond à l'une des amorces du dictionnaire
            answer = answer_beginning + sentence + "." #Ajout de la valeur de l'amorce choisie à la phrase ainsi qu'un point
    return answer
