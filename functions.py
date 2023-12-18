#Calcul du score TF-IDF

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

def mots_uniques(corpus):
    list_of_words = []
    files_names = list_of_files(corpus, "txt")
    #Parcourir chaque fichier de la liste
    for fichier in files_names:
        chemin = os.path.join("./cleaned", fichier)
        with open(chemin, "r", encoding="utf-8") as f1:
            contenu = f1.read()
            mots = contenu.split()
        #Pour chaque mot
        for mot in mots:
            #Ajouter tous les mots de tous les fichiers
            list_of_words.append(mot)
    #Initialiser une liste vide
    unique = []
    #Pour chaque mot de la liste de tous les mots
    for mot in list_of_words:
        #Si le mot n'est pas dans la liste de mots unique
        if mot not in unique:
            #Ajouter le mot
            unique.append(mot)
    return unique

#Création de la matrice TF-IDF

def matrice_TfIdf(corpus,mots_uniques,scores,files_names):
    M = []
    #Utiliser la fonction précédente pour avoir les mots uniques
    liste_mots=mots_uniques(corpus)
    #Pour chaque mot de la liste
    for mot in liste_mots:
        #Initialiser une liste vecteur numérique
        vecteur_num= []
        #Parcourir chaque fichier
        for fichier in files_names:
            #Si le mot est dans le dic des scores TF-IDF
            if mot in scores[fichier]:
                #Ajouter à son vecteur de scores le vecteur numérique
                vecteur_num.append(scores[fichier][mot])
            else:
                #Sinon ajouter un score de 0
                vecteur_num.append(0.0)
        #Ajouter à la matrice le vecteur de scores pour chaque mot
        M.append(vecteur_num)
    return M
