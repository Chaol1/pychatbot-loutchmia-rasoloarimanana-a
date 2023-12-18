"""My first chatbot - LOUTCHMIA Laïli & RASOLOARIMANANA Malalasoa
Fonction qui retourne la liste des présidents mentionnant le terme "nation" et celui qui le nomme le plus."""

# Liste des présidents ayant parlé de la "nation" et celui qui en a le plus parlé
#Paramètres(dic_mat:Matrice TF-IDF dont les clés sont les mots et les valeurs, leur score TF-IDF, list_of_names: Liste des noms des présidents)
#Résultat(noms: chaîne de caractères contenant les noms des présidents parlant de "nation" plus: nom du président qui la mentionne le plus.)

def nation_analyse(dic_mat,list_of_names):
    noms=""
    plus_rep=0.0
    #Parcourir la matrice avec les mots
    for mot,vecteur in dic_mat.items():
        if mot=='nation':
            #Parcourir les valeurs du vecteur du mot nation
            for i in range (len(vecteur)):
                #Parcourir la liste des mots moins importants
                for j in range (len(liste_of_names)):
                    #Si la valeur est différente de 0 et le mot n'est pas dans la liste
                    if vecteur[i]!=0.0 and i==j and liste_of_names[j] not in noms :
                        noms += liste_of_names[j] + " "
                        #Chercher le max
                        if vecteur[i]>plus_rep:
                            plus_rep=vecteur[i]
                            plus=liste_of_names[j]
    return noms,plus
