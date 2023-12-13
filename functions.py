def mots_Chirac(matrice, mots_uniques):
    non_liste=less_important(matrice, mots_uniques)
    mots = []
    plus_rep=0
    with open("cleaned/Nomination_Chirac1.txt", "r", encoding="utf-8") as f1, open("cleaned/Nomination_Chirac2.txt","r", encoding="utf-8") as f2:
        texte1 = f1.read()
        texte2 = f2.read()
    tf1 = tf_chaine(texte1)
    tf2 = tf_chaine(texte2)
    for mot,tf in tf1.items() :
        if tf1[mot]>plus_rep and tf1[mot] not in non_liste:
            plus_rep=tf1[mot]
            mots.append(mot)
    for mot, tf in tf2.items():
        if tf2[mot] > plus_rep and tf2[mot] not in non_liste:
            plus_rep = tf2[mot]
            mots.append(mot)
    return mots

  
