from functions import *

if __name__ == '__main__':

    corpus = "./cleaned"
    speeches = "./speeches"
    corpus_1 = speeches
    question = "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"
    #chosir sa question entre la 1 et la 2
    question2 = "Comment une nation peut-elle prendre soin du climat ?"

    token_question = token(question)
    common=common_words(corpus, question)
    vector_tf_question = quest_final(question, corpus)
    vect_quest=quest_tf_idf(question, corpus)
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)
    similar=calcul_similarity(dic_scores, vect_quest)
    document = doc_plus_pert(question, corpus)
    maxi_word = maxi_tfidf(vect_quest)

    #Fonction à retourner
    sentence = sentence_word(corpus_1, document, maxi_word)
    print("La phrase générée :", sentence)
