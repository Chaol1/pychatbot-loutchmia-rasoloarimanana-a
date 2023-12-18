from functions import *

if __name__ == '__main__':

    corpus = "./cleaned"
    question = "Comment une nation peut-elle prendre soin du climat ?"

    token_question = token(question)
    mots_communs=common_words(corpus, question)
    print("Mots communs : ", mots_communs)
