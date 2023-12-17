# Projet Python L1 : My first Chatbot
Première Partie

### Membres du projet
- LOUTCHMIA Laïli - Groupe A
- RASOLOARIMANANA Malalasoa - Groupe A
 
### Liste des programmes 
#### Fonctions de base
1) **list_of_files(directory, extension)**
2) **surname(files_names)**
3) **first_name(list_of_names)**
4) **without_dubble(list_of_full_names)**
5) **convert_all_texts(files_names)**
6) **convert_all_texts_2(files_names)**

#### Méthode TF-IDF

7) **tf_chaine(texte)**
8) **calcul_tf(corpus)**
9) **nbDocparMot(directory)**
10) **calcul_idf_final()**
11) **tf_idf(dic_TF,dic_IDF)**
12) **mots_uniques(corpus)**
13) **matrice_TfIdf(corpus,dic_scores,files_names)**
14) **matriceAvecMots(corpus, dic_scores, files_names)**

#### Fonctionnalités à développer
15) less_important(TF_IDF,unique)
16) score_eleve(TF_IDF,unique)
17) mots_Chirac(TF_IDF, unique)
18) nation_analyse(dic_mat,liste_of_names)
19) climat_analyse(dic_mat,list_of_names)

### Bugs rencontrés :
- pour *convert_all_texts(files_names)* : à chaque exécution, ne peut pas recréer le répertoire "cleaned".
- pour *calcul_tf(directory)* : retourne un dictionnaire qui a pour clés tous les mots et pour valeurs, le nombre de fois où le mot apparaît dans l'ensemble du corpus et non dans chaque document
- pour Github : à certains moments, nous n'arrivions plus à pull, push ou commit
- Pour "convert_all_texts_2": Problème avec les caractères avec accents malgré une tentative de couvrir la plage de leurs codes ASCII, obligation de passer par une liste exhaustive pour chaque signe de ponctuation. La fonction de base est disponible sous forme de commentaire.

### Instruction d'exécution du code 

La fonction "convert_all_texts" est à exécuter qu'une fois afin d'éviter l'erreur liée à la création du fichier "cleaned". Il faut également enlever les quotes autour des fonctions de base dans le main pour pouvoir les exécuter. Les quotes sont présentes uniquement pour le bon affichage du menu mais sont à enlever pour tester le programme.

### Lien du dépôt GIT

https://github.com/Chaol1/pychatbot-loutchmia-rasoloarimanana-a.git
