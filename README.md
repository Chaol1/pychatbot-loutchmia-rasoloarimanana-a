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
7) calcul_tf(texte)
8) deduplicated_list(corpus)
9) calculf_idf(directory)
10) calcul_idf_final()
    
#### Fonctionnalités à développer
10) makeScore(dicTF,dicIDF)
11) makeMatrixTfIdf(deduplicated,scores,textsNames)
12) orderVectorAsc(matrixTfIdf,deduplicated)
13) orderVectorDesc(matrixTfIdf,deduplicated)
14) chiracAnalysis(corpus)
15) nationAnalysis(corpus)
16) ecologieAnalysis(corpus)
17) allCommonWords(deduplicated,corpus)

### Bugs rencontrés :
- pour *convert_all_texts(files_names)* : à chaque exécution, ne peut pas recréer le répertoire "cleaned".
- pour *calcul_tf(directory)* : retourne un dictionnaire qui a pour clés tous les mots et pour valeurs, le nombre de fois où le mot apparaît dans l'ensemble du corpus et non dans chaque document
- pour Github : à certains moments, nous n'arrivions plus à pull, push ou commit
- Pour "convert_all_texts_2": Problème avec les caractères avec accents malgré une tentative de couvrir la plage de leurs codes ASCII, obligation de passer par une liste exhaustive pour chaque signe de ponctuation. La fonction de base est disponible sous forme de commentaire.

### Instruction d'exécution du code 
