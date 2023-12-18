"""My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonctions de base de traitement des fichiers texte: récupération des noms des présidents & conversion de textes"""


import os

#Fonction qui parcourt la liste des fichiers d’une extension donnée, dans un répertoire donné
#Paramètres(directory: Chemin du répertoire "speeches", extension: extension des fichiers issus de "speeches", ici "txt")
#Résultat(files_names: Liste des noms des fichiers textes contenus dans le répertoire "speeches")

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


#Extraire les noms des présidents à partir des noms des fichiers texte fournis
#Paramètre(files_names: Liste des noms des fichiers texte de "speeches")
#Résultat(list_of_names: Liste des noms de famille des présidents)

def surname(files_names):
    list_of_names=[]
    #Initialiser une chaîne vide
    chain=""
    #Parcourir la liste des noms de fichier
    for i in range(len(files_names)):
        #Réinitialiser la chaine pour stocker le nom à chaque début de la boucle
        chain = ""
        for j in range(len(files_names[i])):
            #A partir de la 1ère lettre du nom (j>=11)
            if j>=11 and j<len(files_names[i])-4 and files_names[i][j]!="1" and files_names[i][j]!="2":
                #Ajouter le caractère à la chaine
                chain+=(files_names[i][j])
        #Ajouter le nom à la liste des noms
        list_of_names.append(chain)
    return(list_of_names)
    

#Associer à chaque président son prénom
#Paramètre(list_of_names: Liste des noms de famille des présidents)
#Résultat(list_of_full_names: Liste des noms et prénoms présidentiels)

def first_name(list_of_names):
    #Initialiser en dur la liste des prénoms
    list_of_first_names=["Jacques ", "Jacques ", "Valéry ", "François ", "Emmanuel ", "François ", "François ", "Nicolas "]
    list_of_full_names=[]
    for i in range(len(list_of_names)):
        #Ajouter à la liste des noms complets la combinaison des prénoms + noms de la liste à la même position
        list_of_full_names.append(list_of_first_names[i]+list_of_names[i])
    return(list_of_full_names)


#Afficher la liste des noms des présidents sans doublons
#Paramètre(list_of_full_names:Liste des noms complets des présidents)
#Résultat(without: Liste des noms et prénoms présidentiels sans doublons)

def without_dubble(list_of_full_names):
    without=[]
    for i in range(len(list_of_full_names)):
        #Si le nom n’est pas déjà dans la liste vide
        if list_of_full_names[i] not in without:
            #Ajouter ce nom à liste
            without.append(list_of_full_names[i])
    return without


#Convertir les textes des 8 fichiers en minuscules + création du répertoire cleaned
#Paramètre(files_names: Liste des fichiers texte de "speeches")
#Résultat(Pas de résultat retourné mais les fichiers texte ont été copiés dans le répertoire "cleaned" et y ont été modifiés)

def convert_all_texts(files_names):
    #Créer le répertoire "cleaned"
    os.mkdir("cleaned")
    line2=""
    #Parcourir les fichiers un à un
    for file in files_names:
        #Créer un chemin vers chaque fichier avec son répertoire
        path1 = os.path.join("./speeches", file)
        path2 = os.path.join("./cleaned", file)
        #Ouvrir les deux fichiers en même temps
        with open(path1, "r") as f1, open(path2, "w") as f2:
            #Pour chaque ligne du fichier ouvert de f1
            for line in f1:
                line2=""
                #Pour chaque caractère de la ligne
                for i in range(len(line)):
                    #Si le code ASCII du caractère est dans l’intervalle des majuscules
                    if (ord(line[i]))>=65 and (ord(line[i]))<=90:
                        #Ajouter à la chaîne le caractère converti en minuscule
                        line2+=chr(ord(line[i]) + 32)
                    else:
                        #Ajouter le caractère si ce n’est pas une majuscule
                        line2+=line[i]
                f2.write(line2)


#Supprimer tous les caractères de ponctuation dans les fichiers de cleaned
#Paramètre(files_names: Liste des noms des fichiers texte partagés de "speeches" et "cleaned")
#Résultat(Pas de résultat retourné mais les fichiers de "cleaned" ont été modifiés.)

def convert_all_texts_2(files_names):
    line1=""
    #Parcourir chaque fichier
    for file in files_names:
        txt = ""
        #Créer un chemin en joignant le répertoire cleaned avec le fichier
        path1=os.path.join("./cleaned", file)
        with open(path1, 'r') as f1:
            content=f1.readlines()
            #Parcourir chaque ligne du contenu du fichier
            for line in content:
                #Parcourir chaque caractère de chaque ligne
                for i in range(len(line)):
                    #Ajouter un espace à la chaîne de caractères si apostrophe ou tiret
                    if (line[i]=="'" or line[i]=="-"):
                        line1+=" "
                    #Si le caractère n’est pas un caractère de ponctuation
                    elif line[i]!="," and line[i]!="." and line[i]!=";" and line[i]!="?" and line[i]!="!" and line[i]!=";" and line[i]!='"'and line[i]!=':':
                        line1+=line[i]
                txt+=line1
                #Réinitialiser la chaîne ligne à une chaîne vide
                line1=""
        f=open(path1, 'w')
        #Ecrire le contenu modifié dans le fichier
        f.write(txt)
        f.close()
