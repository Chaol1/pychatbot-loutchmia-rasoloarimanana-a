# Projet Python L1 : My first Chatbot
Première Partie

### Lien du dépôt GIT

https://github.com/Chaol1/pychatbot-loutchmia-rasoloarimanana-a.git

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

7) **tf_chain(texte)**
8) **calcul_tf(corpus)**
9) **nbDocperWord(directory)**
10) **calcul_idf_final()**
11) **tf_idf(dic_TF,dic_IDF)**
12) **unique_words(corpus)**
13) **matrix_TfIdf(corpus,dic_scores,files_names)**
14) **matrixAvecMots(corpus, dic_scores, files_names)**

#### Fonctionnalités à développer
15) less_important(TF_IDF,unique)
16) high_score(TF_IDF,unique)
17) words_Chirac(TF_IDF, unique)
18) nation_analyse(dic_mat,liste_of_names)
19) climate_names(dic_mat,list_of_names)

### Bugs rencontrés :
- pour *convert_all_texts(files_names)* : à chaque exécution, ne peut pas recréer le répertoire "cleaned".
- pour *calcul_tf(directory)* : retourne un dictionnaire qui a pour clés tous les mots et pour valeurs, le nombre de fois où le mot apparaît dans l'ensemble du corpus et non dans chaque document
- pour Github : à certains moments, nous n'arrivions plus à pull, push ou commit
- Pour "convert_all_texts_2": Problème avec les caractères avec accents malgré une tentative de couvrir la plage de leurs codes ASCII, obligation de passer par une liste exhaustive pour chaque signe de ponctuation. La fonction de base est disponible sous forme de commentaire.

### Instruction d'exécution du code 

La fonction "convert_all_texts" est à exécuter qu'une fois afin d'éviter l'erreur liée à la création du fichier "cleaned". 

### Accéder au menu
Notre menu propose 2 options : 
La première où l'utilisateur choisit un chiffre entre 1 et 5 pour lui afficher les réponses aux 5 fonctionnalités à développer.
La deuxième qui lui permet de poser une question libre.
