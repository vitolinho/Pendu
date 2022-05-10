# 1-
print("""Bienvenue dans le jeu du 

██████  ███████ ███    ██ ██████  ██    ██ 
██   ██ ██      ████   ██ ██   ██ ██    ██ 
██████  █████   ██ ██  ██ ██   ██ ██    ██ 
██      ██      ██  ██ ██ ██   ██ ██    ██ 
██      ███████ ██   ████ ██████   ██████  

choisissez le niveau de difficulté.


0: Difficulté Facile(4 lettres dans le mot à trouvé)
1: Difficulté Moyenne (6 lettres dans le mot à trouvé)
2: Difficulté Difficile (8 lettres dans le mot à trouvé)
3: Quitter """)
player_choice = int(input("Quel difficulté voulez vous? : "))
 # 0 == L4// 1== L6// 2== L8 


# 2-
L4 = ["nike","puma"]
L6 = ["chaton","ballon"]
L8 = ["elephant","pingouin"]

# -----------------------------[PARTIE FONCTIONS POUR LE JEU]------------------------------
# 3-
from random import randint
def word_choosen(L):
    L_hide = ""
    mistery_word = randint(0, 1)
    if mistery_word == 0:
        L_hide = L[0]
    elif mistery_word == 1:
        L_hide = L[1]
    return L_hide


# 4-
def count(L,L_hide):
    i = 0
    count = 0
    while i < len(L_hide) : # L_hide correspond aux choix du mot, donc de l'indice ici
        count = count + 1
        i = i + 1
    return count

#-----------------------------------[FIN DES FONCTIONS]--------------------------------------

if player_choice == 0:
    result4 = word_choosen(L4)
    #print(result4) pour voir si ça fonctionne bien (à enlever à la fin )
    print(len(result4)* " _")
    
    lives = 10
    bonne_rep = []
    mauvaise_rep = []
    compteur_bonne_rep = 0

    while lives > 0:
        answer0 = input("Entrez une lettre pour trouver le mot: ")
        if answer0 not in result4 :
            print("nhin nhin mauvaise réponse .")
            lives = lives - 1
            resultlives = lives
            print(f"Il vous reste {resultlives} essais restants.")
            mauvaise_rep.append(answer0)
            print("Voici les mauvaises lettres: ",mauvaise_rep)
            print(30 * "-")
            if resultlives == 0:
                print("""

██████  ███████ ██████  ██████  ██    ██          
██   ██ ██      ██   ██ ██   ██ ██    ██          
██████  █████   ██████  ██   ██ ██    ██          
██      ██      ██   ██ ██   ██ ██    ██          
██      ███████ ██   ██ ██████   ██████  ██ ██ ██ 
                                                  
                                                  

""")
                break


        elif answer0 in result4 :
            print(f"{answer0} existe dans le mot caché")
            bonne_rep.append(answer0)
            print("Vous avez trouvez les lettres: ",bonne_rep) # réfléchir au tri des lettres
            print(30 * "-")
            compteur_bonne_rep = compteur_bonne_rep + 1
        if compteur_bonne_rep == 4:
            print("""

 ██████   █████   ██████  ███    ██ ███████     ██     
██       ██   ██ ██       ████   ██ ██          ██     
██   ███ ███████ ██   ███ ██ ██  ██ █████       ██     
██    ██ ██   ██ ██    ██ ██  ██ ██ ██                 
 ██████  ██   ██  ██████  ██   ████ ███████     ██     
                                                       
""")
            break
    
            


elif player_choice == 1:
    result6 = word_choosen(L6)
    # print(result6)  pour voir si ça fonctionne bien (à enlever à la fin )
    print(len(result6)* " _")

    lives = 10
    bonne_rep = []
    mauvaise_rep = []
    compteur_bonne_rep = 0

    while lives > 0:
        answer1 = input("Entrez une lettre pour trouver le mot: ")
        if answer1 not in result6 :
            print("nhin nhin mauvaise réponse .")
            lives = lives - 1
            resultlives = lives
            print(f"Il vous reste {resultlives} essais restants.")
            mauvaise_rep.append(answer1)
            print("Voici les mauvaises lettres: ",mauvaise_rep)
            print(30 * "-")
            if resultlives == 0:
                print("""

██████  ███████ ██████  ██████  ██    ██          
██   ██ ██      ██   ██ ██   ██ ██    ██          
██████  █████   ██████  ██   ██ ██    ██          
██      ██      ██   ██ ██   ██ ██    ██          
██      ███████ ██   ██ ██████   ██████  ██ ██ ██ 
                                                  
                                                  

""")
                break

        elif answer1 in result6 :
            print(f"{answer1} existe dans le mot caché")
            bonne_rep.append(answer1)
            print("Vous avez trouvez les lettres: ",bonne_rep) # réfléchir au tri des lettres
            print(30 * "-")
            compteur_bonne_rep = compteur_bonne_rep + 1
        if compteur_bonne_rep == 6:
            print("""

 ██████   █████   ██████  ███    ██ ███████     ██     
██       ██   ██ ██       ████   ██ ██          ██     
██   ███ ███████ ██   ███ ██ ██  ██ █████       ██     
██    ██ ██   ██ ██    ██ ██  ██ ██ ██                 
 ██████  ██   ██  ██████  ██   ████ ███████     ██     
                                                       
""")
            break


elif player_choice == 2:
    result8 = word_choosen(L8)
    # print(result8)
    print(len(result8)* " _")
    
    lives = 10
    bonne_rep = []
    mauvaise_rep = []
    compteur_bonne_rep = 0
    
    while lives > 0:
        answer2 = input("Entrez une lettre pour trouver le mot: ")
        if answer2 not in result8 :
            print("nhin nhin mauvaise réponse .")
            lives = lives - 1
            resultlives = lives
            print(f"Il vous reste {resultlives} essais restants.")
            mauvaise_rep.append(answer2)
            print("Voici les mauvaises lettres: ",mauvaise_rep)
            print(30 * "-")
            if resultlives == 0:
                print("""

██████  ███████ ██████  ██████  ██    ██          
██   ██ ██      ██   ██ ██   ██ ██    ██          
██████  █████   ██████  ██   ██ ██    ██          
██      ██      ██   ██ ██   ██ ██    ██          
██      ███████ ██   ██ ██████   ██████  ██ ██ ██ 
                                                  
                                                  

""")
                break

        elif answer2 in result8 :
            print(f"{answer2} existe dans le mot caché")
            bonne_rep.append(answer2)
            print("Vous avez trouvez les lettres: ",bonne_rep) # réfléchir au tri des lettres
            print(30 * "-")
            compteur_bonne_rep = compteur_bonne_rep + 1
        if compteur_bonne_rep == 8:
            print("""

 ██████   █████   ██████  ███    ██ ███████     ██     
██       ██   ██ ██       ████   ██ ██          ██     
██   ███ ███████ ██   ███ ██ ██  ██ █████       ██     
██    ██ ██   ██ ██    ██ ██  ██ ██ ██                 
 ██████  ██   ██  ██████  ██   ████ ███████     ██     
                                                       
""")
            break
    
elif player_choice == 3:
    print("A bientôt !!")