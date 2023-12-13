#Calcul du score IDF

def nbDocparMot(directory):
    dico={}
    files_names=list_of_files(directory, "txt")
    contenu_fichier = []
    for fichier in files_names:
        chemin=os.path.join("./cleaned", fichier)
        with open(chemin, "r",encoding="utf-8") as f1:
            #Stockage dans une variable, du contenu d'un fichier texte
            contenu=f1.read()
            #Sépare chaque mot du texte dans une liste
            mots=contenu.split()
        #Parcourir chaque élément de la liste "mots"
        for elt in mots:
            #liste permet de savoir si élément déjà rencontré dans le fichier
            if elt in dico and elt not in contenu_fichier:
                dico[elt] += 1.0
                contenu_fichier.append(elt)
            #Quand l'élément n'est pas encore dans le dico
            elif (elt not in dico):
                dico[elt] = 1.0
                contenu_fichier.append(elt)
        #Réinitialisation de la liste pour chaque changement de fichier
        contenu_fichier = []
    return dico

def calcul_idf_final():
    #Utilisation de la fonction précédente
    dico=nbDocparMot("./cleaned")
    #Récupérer la liste de fichiers du répertoire
    fichiers=list_of_files("./cleaned", "txt")
    #Parcourir le dictionnaire avec a : clé et b : valeur
    for (a,b) in dico.items():
        #Calcul du logarithme décimal de l'inverse de la proportion
        dico[a]=math.log10(len(fichiers)/b)
    return dico


