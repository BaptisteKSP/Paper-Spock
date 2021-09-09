import random
import os
def PierreSpock(nombreJoueur):

    if(nombreJoueur < 0 or nombreJoueur > 4 or type(nombreJoueur) != int):
        while(nombreJoueur < 0 or nombreJoueur > 4 or type(nombreJoueur) != int):
            print("Le nombre donné est incorrect")
            nombreJoueur = int(input())

    #attaque = {0:"Pierre", 1:"Papier", 2:"Ciseaux", 3:"Lezard", 4:"Spock"}
    nombreBot = random.randint(0, 4)
    while(nombreJoueur == nombreBot):
        nombreBot = random.randint(0, 4)
    Result(nombreJoueur, nombreBot)

def Result(nombreJ, nombreB):

    tab = []

    for x in range(44):
        tab.append(0)

    tab[1] = 2
    tab[2] = 2
    tab[3] = 1
    tab[4] = 1
    tab[10] = 1
    tab[12] = 2
    tab[13] = 1
    tab[14] = 1
    tab[20] = 1
    tab[21] = 2
    tab[23] = 1
    tab[24] = 2
    tab[30] = 2
    tab[31] = 1
    tab[32] = 2
    tab[34] = 1
    tab[40] = 2
    tab[41] = 1
    tab[42] = 1
    tab[43] = 2

    nb = int(nombreJ + nombreB)

    if(tab[nb] == 1):
        print("Le joueur a gagné")
    else:
        print("Vous avez perdu contre le bot :'(")
    print("La partie recommence")
    Begin()

def Begin():
    print("Veuillez rentrer un nombre entre 0 et 4")
    nb = input()
    PierreSpock(int(nb))

Begin()





    