""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonction qui retourne le fichier qui a la similarité la plus proche du vecteur de la question"""


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
