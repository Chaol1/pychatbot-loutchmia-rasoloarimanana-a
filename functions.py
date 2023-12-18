""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonction qui "tokenise" les termes d'une question"""

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
