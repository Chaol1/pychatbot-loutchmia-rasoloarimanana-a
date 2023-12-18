# main_second.py

""" My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Le fichier main_second.py permet de tester toutes les fonctions utilisées dans la partie 2 avec un affichage plus clair pour se retrouver,
il ne s'agit pas encore du menu mais facilite la compréhenison du code."""


from functions2 import *

if __name__ == '__main__':

    corpus = "./cleaned"
    speeches = "./speeches"
    corpus_1 = speeches
    question = "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
    #chosir sa question entre la 1 et la 2
    question2 = "Comment une nation peut-elle prendre soin du climat ?"

    token_question = token(question)
    print("Liste token : ", token_question)

    common=common_words(corpus, question)
    print("Liste mots commun entre corpus et question :", common)

    tf_question_a_0 = tf_chaine_bis(question)
    print("Dic TF question de ses mots initialisé à 0:", tf_question_a_0)

    tf_question = calcul_tf_bis(corpus)
    print("Dic TF question avec les mots du corpus initialisé à 0: :", tf_question)

    vector_tf_question = quest_final(question, corpus)
    print("Dic Vecteur de la question avec TF :", vector_tf_question)

    vect_quest=quest_tf_idf(question, corpus)
    print("Vecteur final TF-IDF de la question :", vect_quest)

    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)

    similar=calcul_similarity(dic_scores, vect_quest)
    print("Dic Similarité entre vecteur question et chaque N document :", similar)

    document = doc_plus_pert(question, corpus)
    print("Document pertinent retourné :", document)

    maxi_word = maxi_tfidf(vect_quest)
    print("Mot ayant le TF-IDF le plus élevé :", maxi_word)

    sentence = sentence_word(corpus_1, document, maxi_word)
    print("La phrase générée :", sentence)

    answer = answer_chatbot(question,sentence)
    print("La réponse du chatBot est :", answer)
