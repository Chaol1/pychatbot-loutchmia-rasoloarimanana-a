""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier 'mot_question_max'' permet d'afficher le mot de la question avec le score tf-idf le plus élevé"""

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
