import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print("_|_".join(ligne))
    print()

def verifier_victoire(plateau, symbole):
    #verifier si il y'a une victoire ou pas
    for i in range(3):
        if all(plateau[i][j] == symbole for j in range(3)) or all(plateau[j][i] == symbole for j in range(3)):
            return True
    if all(plateau[i][i] == symbole for i in range(3)) or all(plateau[i][2 - i] == symbole for i in range(3)):
        return True
    return False

def est_case_valide(plateau, ligne, colonne):
    #pour verifier si la position ests deja jouer ou pas
    return 0 <= ligne < 3 and 0 <= colonne < 3 and plateau[ligne][colonne] == " "

def jouer_bot(plateau, symbole_utilisateur):
    #verifier si peut gagner
    for i in range(3):
        #verifier les ligne
        if plateau[i].count("O") == 2 and plateau[i].count(" ") == 1:
            return i, plateau[i].index(" ")

        #verifier les colones
        colonne = [plateau[j][i] for j in range(3)]
        if colonne.count("O") == 2 and colonne.count(" ") == 1:
            return colonne.index(" "), i

    #verifier les diagonale
    diag1 = [plateau[i][i] for i in range(3)]
    if diag1.count("O") == 2 and diag1.count(" ") == 1:
        return diag1.index(" "), diag1.index(" ")

    diag2 = [plateau[i][2 - i] for i in range(3)]
    if diag2.count("O") == 2 and diag2.count(" ") == 1:
        if "" in diag2:
            return diag2.index(""), 2 - diag2.index("")

    #verfier pour defendre
    for i in range(3):
        #defendre ligne
        if plateau[i].count(symbole_utilisateur) == 2 and plateau[i].count(" ") == 1:
            return i, plateau[i].index(" ")

        #defendre colone
        colonne = [plateau[j][i] for j in range(3)]
        if colonne.count(symbole_utilisateur) == 2 and colonne.count(" ") == 1:
            return colonne.index(" "), i

    #defendre les diagonales
    diag1 = [plateau[i][i] for i in range(3)]
    if diag1.count(symbole_utilisateur) == 2 and diag1.count(" ") == 1:
        return diag1.index(" "), diag1.index(" ")

    diag2 = [plateau[i][2 - i] for i in range(3)]
    if diag2.count(symbole_utilisateur) == 2 and diag2.count(" ") == 1:
        if "" in diag2:
            return diag2.index(""), 2 - diag2.index("")

    #si ne defend pas et n'attaque pas faire un moove aleatoire
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if est_case_valide(plateau, ligne, colonne):
            return ligne, colonne


def rejouer():
    #demander aux joueur si il veux rejouer a la fin
    while True:
        choix = input("vous voulez rejouer ? (oui/non): ").lower()
        if choix == "oui":
            return True
        elif choix == "non":
            return False
        else:
            print("la reponse doit etre 'oui' ou 'non'.")

def jouer():
    while True:
        plateau = [[" " for _ in range(3)] for _ in range(3)]
        tour_utilisateur = True

        while True:
            afficher_plateau(plateau)

            if tour_utilisateur:
                try:
                    colonne = int(input("entrez le numéro de colonne (1, 2, 3) : ")) - 1
                    ligne = int(input("entrez le numéro de ligne (1, 2, 3) : ")) - 1
                except ValueError:
                    print("veuillez entrer des nombres valide entre(1, 2, 3)!!!.")
                    continue

                if est_case_valide(plateau, ligne, colonne):
                    plateau[ligne][colonne] = "X"
                    if verifier_victoire(plateau, "X"):
                        afficher_plateau(plateau)
                        print("vous avez gagne bravooooo")
                        break
                    tour_utilisateur = False
                else:
                    print("la case est deja jouer. Veuillez reesayer .")

            else:
                ligne, colonne = jouer_bot(plateau, "X")  # x est le symbole de l'utilisateur
                plateau[ligne][colonne] = "O"
                if verifier_victoire(plateau, "O"):
                    afficher_plateau(plateau)
                    print("Le bot a gagner. vous etes trop nulllle")
                    break
                tour_utilisateur = True

            if all(plateau[i][j] != " " for i in range(3) for j in range(3)):
                afficher_plateau(plateau)
                print("match nul(draww) !")
                break

        if not rejouer():
            break

jouer()

