# PARTIE 1

import os

#Fonction qui parcourt la liste des fichiers d’une extension donnée, dans un répertoire donné
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#Extraire les noms des présidents à partir des noms des fichiers texte fournis

def surname(files_names):
    list_of_names=[]
    #Initialiser une chaîne vide
    chaine=""
    #Parcourir la liste des noms de fichier
    for i in range(len(files_names)):
        #Réinitialiser la chaine pour stocker le nom à chaque début de la boucle
        chaine = ""
        for j in range(len(files_names[i])):
            #A partir de la 1ère lettre du nom (j>=11)
            #Sans l'extension (.txt) et sans les chiffres 1 et 2
            if j>=11 and j<len(files_names[i])-4 and files_names[i][j]!="1" and files_names[i][j]!="2":
                #Ajouter le caractère à la chaine
                chaine+=(files_names[i][j])
        #Ajouter le nom à la liste des noms
        list_of_names.append(chaine)
    return(list_of_names)

#Associer à chaque président un prénom

def first_name(list_of_names):
    #Initialiser en dur la liste des prénoms
    list_of_first_names=["Jacques ", "Jacques ", "Valéry ", "François ", "Emmanuel ", "François ", "François ", "Nicolas "]
    list_of_full_names=[]
    for i in range(len(list_of_names)):
        #Ajouter à la liste des noms complets la combinaison des prénoms + noms de la liste à la même position
        list_of_full_names.append(list_of_first_names[i]+list_of_names[i])
    return(list_of_full_names)

#Afficher la liste des noms des présidents sans doublons

def without_dubble(list_of_full_names):
    without=[]
    for i in range(len(list_of_full_names)):
        #Si le nom n’est pas déjà dans la liste vide
        if list_of_full_names[i] not in without:
            #Ajouter ce nom à liste
            without.append(list_of_full_names[i])
    return without

#Convertir les textes des 8 fichiers en minuscules + création du répertoire cleaned

def convert_all_texts(files_names):
    #Créer le répertoire "cleaned"
    os.mkdir("cleaned")
    ligne2=""
    #Parcourir les fichiers un à un
    for fichier in files_names:
        #Créer un chemin vers chaque fichier avec son répertoire
        chemin = os.path.join("./speeches", fichier)
        chemin2 = os.path.join("./cleaned", fichier)
        #Ouvrir les deux fichiers en même temps
        with open(chemin, "r") as f1, open(chemin2, "w") as f2:
            #Pour chaque ligne du fichier ouvert de f1
            for ligne in f1:
                ligne2=""
                #Pour chaque caractère de la ligne
                for i in range(len(ligne)):
                    #Si le code ASCII du caractère est dans l’intervalle des majuscules
                    if (ord(ligne[i]))>=65 and (ord(ligne[i]))<=90:
                        #Ajouter à la chaîne le caractère convertit en minuscule
                        ligne2+=chr(ord(ligne[i]) + 32)
                    else:
                        #Ajouter le caractère si ce n’est pas une majuscule
                        ligne2+=ligne[i]
                f2.write(ligne2)


#Supprimer tous les caractères de ponctuation dans les fichiers de cleaned
def convert_all_texts_2(files_names):
    ligne1=""
    #Parcourir chaque fichier
    for fichier in files_names:
        txt = ""
        #Créer un chemin en joignant le répertoire cleaned avec le fichier
        chemin=os.path.join("./cleaned", fichier)
        with open(chemin, 'r') as f1:
            #Lire toutes les lignes du fichier
            contenu=f1.readlines()
            #Parcourir chaque ligne du contenu du fichier
            for ligne in contenu:
                #Parcourir chaque caractère de chaque ligne
                for i in range(len(ligne)):
                    #Si le caractère correspond à une apostrophe ou un tiret
                    #Ajouter un espace à la chaîne de caractères
                    if (ligne[i]=="'" or ligne[i]=="-"):
                        ligne1+=" "
                    #Si le caractère n’est pas un caractère de ponctuation
                    elif ligne[i]!="," and ligne[i]!="." and ligne[i]!=";" and ligne[i]!="?" and ligne[i]!="!" and ligne[i]!=";" and ligne[i]!='"'and ligne[i]!=':':
                        ligne1+=ligne[i]
                txt+=ligne1
                #Réinitialiser la chaîne ligne à un chaîne vide
                ligne1=""
        #Ouvrir le fichier en mode écriture
        f=open(chemin, 'w')
        #Ecrire le contenu modifié dans le fichier
        f.write(txt)
        f.close()
