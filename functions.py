def ecologie_climat(corpus, mots_uniques, scores, files_names):
    mat=matriceAvecMots(corpus, mots_uniques, scores, files_names)
    cpt=0
    print(mat["climat"])
    for i in range (len(mat["climat"])):
        if mat["climat"][i]!=0.0:
            cpt=i
    list1=surname(files_names)
    return (list1[cpt])
