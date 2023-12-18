""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonction qui améliore les réponses apportées par le chatbot"""

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

