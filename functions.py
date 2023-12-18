""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier phrase_avec_mot.py retourne la première phrase qui contient le mot de la question avec le score TF-IDF le plus élevé """

#Fonction 'sentence_word' qui prend en paramètres :
#(corpus : le répertoire de documents, document :le document le plus pertinent, maxi_wird : le mot avec les max score)
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

