# PARTIE 1

import os

#Fonction qui parcourt la liste des fichiers d’une extension donnée, dans un répertoire donné
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#Fonction qui permet d'avoir les fichiers du corpus sous forme de liste
def get_texts_from_documents(directory):
    corpus = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            corpus.append(file.read().split())
    return corpus

#Extraire les noms des présidents à partir des noms des fichiers texte fournis
def surname(files_names):
    list_of_names=[]
    chaine=""
    for i in range(len(files_names)):
        chaine = ""
        for j in range(len(files_names[i])):
            if j>=11 and j<len(files_names[i])-4 and files_names[i][j]!="1" and files_names[i][j]!="2":
                chaine+=(files_names[i][j])
        list_of_names.append(chaine)
    return(list_of_names)

#Associer à chaque président un prénom
def first_name(list_of_names):
    list_of_first_names=["Jacques ", "Jacques ", "Valéry ", "François ", "Emmanuel ", "François ", "François ", "Nicolas "]
    list_of_full_names=[]
    for i in range(len(list_of_names)):
        list_of_full_names.append(list_of_first_names[i]+list_of_names[i])
    return(list_of_full_names)


#Afficher la liste des noms des présidents sans doublons
def without_dubble(list_of_full_names):
    without=[]
    for i in range(len(list_of_full_names)):
        if list_of_full_names[i] not in without:
            without.append(list_of_full_names[i])
    return without

#Convertir les textes des 8 fichiers en minuscules + création du répertoire cleaned
def convert_all_texts(files_names):
    os.mkdir("cleaned")
    ligne2=""
    for fichier in files_names:
        chemin = os.path.join("./speeches", fichier)
        chemin2 = os.path.join("./cleaned", fichier)
        with open(chemin, "r") as f1, open(chemin2, "w") as f2:
            for ligne in f1:
                ligne2=""
                for i in range(len(ligne)):
                    if (ord(ligne[i]))>=65 and (ord(ligne[i]))<=90:
                        ligne2+=chr(ord(ligne[i]) + 32)
                    else:
                        ligne2+=ligne[i]
                f2.write(ligne2)

#Supprimer tous les caractères de ponctuation dans les fichiers de cleaned
def convert_all_texts_2(files_names):
    ligne1=""
    for fichier in files_names:
        txt = ""
        chemin=os.path.join("./cleaned", fichier)
        with open(chemin, 'r') as f1:
            contenu=f1.readlines()
            for ligne in contenu:
                for i in range(len(ligne)):
                    if (ligne[i]=="'" or ligne[i]=="-"):
                        ligne1+=" "
                    elif ligne[i]!="," and ligne[i]!="." and ligne[i]!=";" and ligne[i]!="?" and ligne[i]!="!" and ligne[i]!=";" and ligne[i]!='"'and ligne[i]!=':':
                        ligne1+=ligne[i]
                txt+=ligne1
                ligne1=""
        f=open(chemin, 'w')
        f.write(txt)
        f.close()


# Calcul de TF pour chaque mot dans chaque document
def calcul_tf(texte):
    dictMotsOccurence = {}
    for mot in texte:
        if mot in dictMotsOccurence:
            dictMotsOccurence[mot] +=1
        else:
            dictMotsOccurence[mot] = 1
    return dictMotsOccurence

# Calcul de IDF
import math

def deduplicated_list(corpus): #liste_sans_doublons
    list_of_words = []
    for texte in corpus:
        for mot in texte:
            list_of_words.append(mot)#tous les mots de tous les textes
    deduplicated = []
    for mot in list_of_words:
        if mot not in deduplicated:
            deduplicated.append(mot)
    return deduplicated

def calculf_idf(directory):
    dico={}
    files_names=list_of_files(directory, "txt")
    contenu_fichier = []
    for fichier in files_names:
        chemin=os.path.join("./cleaned", fichier)
        with open(chemin, "r",encoding="utf-8") as f1:
            contenu=f1.read() #stockage dans une variable, du contenu d'un fichier texte
            mots=contenu.split() # split de chaque mot du texte dans une liste
        for elt in mots: # cas par cas, pour chaque élément de la liste "mots"
            if elt in dico and elt not in contenu_fichier: #liste permet de savoir si élément déjà rencontré dans le fichier
                dico[elt] += 1.0
                contenu_fichier.append(elt)
            elif (elt not in dico): #quand l'élément n'est pas encore dans le dico
                dico[elt] = 1.0
                contenu_fichier.append(elt)
        contenu_fichier = [] #réinitialisation de la liste pour chaque changement de fichier
    return dico

def calcul_idf_final():
    dico=calculf_idf("./cleaned")
    fichiers=list_of_files("./cleaned", "txt") #liste de fichiers
    for (a,b) in dico.items(): # a est la clé et b, la valeur
        dico[a]=math.log10(len(fichiers)/b)+1
    return dico

#Matrice TF-IDF


def makeScore(dicTF,dicIDF):
    scores = {}
    for textsName,texte in dicTF.items():
        scores[textsName] = {}
        for mot,iteration in texte.items():
            scores[textsName][mot] = iteration * dicIDF[mot]
    return scores


def makeMatrixTfIdf(deduplicated,scores,textsNames):
    matrixTfIDF = []
    for mot in deduplicated:
        oneMotVector = []
        for oneDocument in textsNames:
            if mot in scores[oneDocument]:
                oneMotVector.append(scores[oneDocument][mot])
            else:
                oneMotVector.append(0)
        matrixTfIDF.append(oneMotVector)
    return matrixTfIDF

def orderVectorAsc(matrixTfIdf,deduplicated):
    wordWithVector={}
    j=0
    for vector in matrixTfIdf:
        wordWithVector[deduplicated[j]] = sum(vector)
        j+=1
    listAsc = dict(sorted(wordWithVector.items(),key=lambda item: item[1]))
    return list(listAsc.keys())[:10]

def orderVectorDesc(matrixTfIdf,deduplicated):
    wordWithVector={}
    j=0
    for vector in matrixTfIdf:
        wordWithVector[deduplicated[j]] = sum(vector)
        j+=1
    dictDesc = dict(sorted(wordWithVector.items(),key=lambda item: item[1], reverse=True))
    return list(dictDesc.keys())[:10]

def chiracAnalysis(corpus):
    texte1 = corpus[0]
    texte2 = corpus[1]
    texte1occurence = calcul_tf(texte1)
    texte2occurence = calcul_tf(texte2)

    merged = {}
    for key in texte1occurence:
        merged[key] = merged.get(key,0)+ texte1occurence[key]
    for key in texte2occurence:
        merged[key] = merged.get(key,0)+ texte2occurence[key]
    mergedDesc = dict(sorted(merged.items(),key=lambda item: item[1], reverse=True))

    return dict(list(mergedDesc.items())[:10])

def nationAnalysis(corpus):
    i=0
    listPresidentsNation = {}
    for texte in corpus:
        if 'nation' in texte:
            nbTimesNationInThisText = texte.count('nation')
            if i == 0 or i == 1:#chirac
                listPresidentsNation["Chirac"] = listPresidentsNation.get('Chirac',0) + nbTimesNationInThisText
            elif i == 2:
                listPresidentsNation["Giscard"] = listPresidentsNation.get('Giscard',0) + nbTimesNationInThisText
            elif i == 3:
                listPresidentsNation["Holland"] = listPresidentsNation.get('Holland',0) + nbTimesNationInThisText
            elif i == 4:
                listPresidentsNation["Macron"] = listPresidentsNation.get('Macron',0) + nbTimesNationInThisText
            elif i == 5 or i == 6:
                listPresidentsNation["Mitterand"] = listPresidentsNation.get('Mitterand',0) + nbTimesNationInThisText
            elif i == 7:
                listPresidentsNation["Sarkozy"] = listPresidentsNation.get('Sarkozy',0) + nbTimesNationInThisText
        i+=1

    return listPresidentsNation

def ecologieAnalysis(corpus):
    i=0
    listPresidentsEcologie = {}
    for texte in corpus:
        j=0
        if 'climat' in texte:
            index = texte.index('climat')
            if i == 0 or i == 1:#chirac
                listPresidentsEcologie["Chirac"] = index
            elif i == 2:
                listPresidentsEcologie["Giscard"] = index
            elif i == 3:
                listPresidentsEcologie["Holland"] = index
            elif i == 4:
                listPresidentsEcologie["Macron"] = index
            elif i == 5 or i == 6:
                listPresidentsEcologie["Mitterand"] = index
            elif i == 7:
                listPresidentsEcologie["Sarkozy"] = index
        i+=1

    return listPresidentsEcologie

def allCommonWords(deduplicated,corpus):
    commonWords = []
    for mot in deduplicated:
        if mot in (corpus[0] or corpus[1]) and mot in corpus[2] and mot in corpus[3] and mot in corpus[4] and (mot in corpus[5] or mot in corpus[6]) and mot in corpus[7]:
            commonWords.append(mot)
    return commonWords
