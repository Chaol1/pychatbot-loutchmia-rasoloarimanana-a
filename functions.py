"""My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Création du dictionnaire des scores TF-IDF et de la matrice TF-IDF"""

#Calcul du score TF-IDF
#Paramètres(dicTF: dictionnaire contenant les scores TF de chaque mot, dicIDF: dictionnaire contenant les scores IDF de chaque mot)
#Résultat(scores: dictionnaire contenant les scores TF-IDF de chaque mot)

def tf_idf(dicTF,dicIDF):
    scores = {}
    #Parcourir le dictionnaire TF
    for file,dicOcc in dicTF.items():
        scores[file] = {}
        #Parcourir le dictionnaire valeur du dicTF
        for word,tf in dicOcc.items():
            #Calcul du score TF-IDF pour chaque mot
            scores[file][word] = tf * dicIDF[word]
    return scores


# Liste des mots dédupliqués
#Paramètre(corpus: chemin du dossier "cleaned")
#Résultat(unique: Liste des mots de chaque document sans doublon)

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
#Paramètres(corpus: chemin du répertoire "cleaned", scores: dictionnaire contenant les scores TF-IDF de chaque mot, files_names: Liste des noms des fichiers texte dans "cleaned")
#Résultat(M:Matrice TF-IDF)

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
