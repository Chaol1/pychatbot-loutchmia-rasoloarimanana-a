from functions import * 
#Importer aussi les fonctions des branches tf, IDF et tf_idf_quest pour avoir dic_TF, dic_IDF et dic_scores

if __name__ == '__main__':

    corpus = "./cleaned"
    speeches = "./speeches"
    question = "Comment une nation peut-elle prendre soin du climat ?"

    token_question = token(question)
    common=common_words(corpus, question)
    vect_quest=quest_tf_idf(question, corpus)
    dic_TF = calcul_tf(corpus)
    dic_IDF = calcul_idf_final()
    dic_scores = tf_idf(dic_TF, dic_IDF)

    similar=calcul_similarity(dic_scores, vect_quest)
    document = doc_plus_pert(question, corpus)
    
    #Fonction qui nous intéresse
    maxi_word = maxi_tfidf(vect_quest)
    print("Mot ayant le TF-IDF le plus élevé :", maxi_word)
