from functions import * #De la branche main pour avoir dic_TF, dic_IDF et dic_scores

if __name__ == '__main__':

    corpus = "./cleaned"
    speeches = "./speeches"
    question = "Comment une nation peut-elle prendre soin du climat ?"
    token_question = token(question)
    mots_communs=common_words(corpus, question)
    vect_quest=quest_tf_idf(question, corpus)
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)

    similarite=calcul_similarity(dic_scores, vect_quest)
    print("Similarité entre vecteur de la question et chaque N document :", similarite)
