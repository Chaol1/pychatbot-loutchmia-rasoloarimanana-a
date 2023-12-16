# Score le plus élevé
def score_eleve(mat):
    maxi=""
    max_tfidf=0
    for nom, vecteur in mat.items():
        for i in range (len(vecteur)):
            if vecteur[i]>max_tfidf:
                max_tfidf=vecteur[i]
                mot=nom
                maxi+= mot + " "
    return maxi
