def ecologie_climat(corpus, mots_uniques, scores, files_names):
    mat=matriceAvecMots(corpus, mots_uniques, scores, files_names) #Matrice TF-IDF formatée avec le mot et son score TF-IDF
    cpt=0 
    for i in range (len(mat["climat"])): #Liste contenant les scores TF-IDF de chaque document sur le mot "climat" 
        if mat["climat"][i]!=0.0:
            cpt=i
    list1=surname(files_names) #Liste des noms de présidents
    return (list1[cpt]) #Retourne le nom du président qui parle de "climat"
