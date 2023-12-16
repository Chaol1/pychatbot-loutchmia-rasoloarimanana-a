# Mot le plus dit par Chirac
def mots_Chirac(matrice, mots_uniques):
    non_liste = less_important(matrice, mots_uniques)
    mots = ""
    plus_rep_1 = 0
    plus_rep_2 = 0
    with open("cleaned/Nomination_Chirac1.txt", "r", encoding="utf-8") as f1, open("cleaned/Nomination_Chirac2.txt", "r", encoding="utf-8") as f2:
        texte1 = f1.read()
        texte2 = f2.read()
    tf1 = tf_chaine(texte1)
    tf2 = tf_chaine(texte2)
    # Parcourir le premier fichier
    for mot, tf in tf1.items():
        # Si le tf du mot est supérieur au tf de base et qu'iln'est pas dans la liste
        if tf > plus_rep_1 and mot not in non_liste:
            plus_rep_1 = tf
            mots = mot
        elif tf == plus_rep_1 and mot not in non_liste:
            mots+= mot
    # Parcourir le deuxième fichier
    for mot, tf in tf2.items():
        if tf > plus_rep_2 and mot not in non_liste :
            plus_rep_2 = tf
            mots = mot
        elif tf == plus_rep_2 and mot not in non_liste :
            mots+=mot
    return mots
