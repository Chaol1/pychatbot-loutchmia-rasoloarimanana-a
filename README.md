# Projet Python L1 : My first Chatbot

### Membres du projet
- LOUTCHMIA Laïli - Groupe A
- RASOLOARIMANANA Malalasoa - Groupe A
 
### Lien du dépôt GIT
https://github.com/Chaol1/pychatbot-loutchmia-rasoloarimanana-a.git

### Rapport du projet en pdf : 
Rapport_pychatbot-rasoloarimanana-loutchmia-a.pdf (dans le document .zip)

### Accéder au menu
!!! Pour pouvoir tester l'ensemble des fonctions et le chatbot, il est important de n'éxecuter **que les deux fonctions suivantes** que nous avons créer :
- *chatbot_officiel_loutchmia_rasoloarimanana.py*
- *menu_all.py* 

 Le menu propose 2 options.
 
La première où l'utilisateur choisit un chiffre entre 1 et 5 pour lui afficher les réponses aux 5 fonctionnalités à développer.
La deuxième qui lui permet de poser une question libre.
Lorsqu'on demande "Votre choix : ", soit vous mettez un chiffre, soit vous écrivez votre question commençant par une **majuscule** et par ces mots : *"Comment","Pourquoi","Peux-tu","Quel","Quels" ou "Quand"*. 

Vous aurez ainsi une réponse complète basée sur les documents.
### Liste des programmes 
#### Fonctions de base
1) list_of_files(directory, extension)
2) surname(files_names)
3) first_name(list_of_names)
4) without_dubble(list_of_full_names)
5) convert_all_texts(files_names)
6) convert_all_texts_2(files_names)

#### Méthode TF-IDF

7) tf_chain(texte)
8) calcul_tf(corpus)
9) nbDocperWord(directory)
10) calcul_idf_final()
11) tf_idf(dic_TF,dic_IDF)
12) unique_words(corpus)
13) matrix_TfIdf(corpus,dic_scores,files_names)
14) matrixWithWords(corpus, dic_scores, files_names)

#### Fonctionnalités à développer
15) less_important(TF_IDF,unique)
16) high_score(TF_IDF,unique)
17) words_Chirac(TF_IDF, unique)
18) nation_analyse(dic_mat,list_of_names)
19) climate_names(dic_mat,list_of_names)

#### Vectorisation de question
20) token(question)
21) common_words (corpus, question)
22) tf_chain_bis(text)
23) calcul_tf_bis(corpus)
24) quest_final(question, corpus)
25) quest_tf_idf(question, corpus)

#### Calcul de la similarité
27) scalar_product(vectA,vectB)
28) norm_vector(vect)
29) general_similarity(scalar_product, normA, normB)
30) calcul_similarity(dic_scores, vect_quest)

#### Génération de réponse automatique
32) doc_plus_pert(question, corpus)
33) maxi_tfidf(vect_quest)
34) sentence_word(corpus, document, maxi_word)
35) answer_chatbot(question,sentence)

### Bugs rencontrés :
- Pour *"convert_all_texts(files_names)"* : à chaque exécution, ne peut pas recréer le répertoire "cleaned".
- Pour *"calcul_tf(directory)"* : retourne un dictionnaire qui a pour clés tous les mots et pour valeurs, le nombre de fois où le mot apparaît dans l'ensemble du corpus et non dans chaque document
- Pour Github : à certains moments, nous n'arrivions plus à pull, push ou commit
- Pour *"convert_all_texts_2(files_names)"*: Problème avec les caractères avec accents malgré une tentative de couvrir la plage de leurs codes ASCII, obligation de passer par une liste exhaustive pour chaque signe de ponctuation. La fonction de base est disponible sous forme de commentaire.
- Pour *"answer_chatbot(question,sentence)"* : Problème pour certaines questions données par l'utilisateur, une concaténation impossible entre "str" et "None" si la phrase est trop longue ou si elle contient des mots récurrents, il faut donc essayer avec des questions comme "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?" ou "Comment une nation peut-elle prendre soin du climat ?" pour que cela fonctionne.

Nous avons majoritairement opté pour des matrices sous forme de dictionnaire car cela permet de mieux visualiser pour chaque document, chaque mot et sa valeur et le parcours avec les items nous semble plus simple.

### Instruction d'exécution du code 

- La fonction "convert_all_texts" est à exécuter qu'une fois afin d'éviter l'erreur liée à la création du fichier "cleaned".
- Si vous voulez tester toutes les fonctions de la **première partie** sans forcément afficher le menu, exécutez le main.py.
- Si vous voulez tester toutes les fonctions de la **seconde partie** sans forcément afficher le menu, exécutez le main_second.py.
- Plusieurs fonctions ont besoin des fonctions précédentes, il est donc nécessaire de les définir avant, si elles appartiennent à d'autres branches.


