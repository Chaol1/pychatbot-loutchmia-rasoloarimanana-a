""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonction qui "tokenise" les termes d'une question"""

# Calcul du vecteur TF-IDF pour les termes de la question

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

