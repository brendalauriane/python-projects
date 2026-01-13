# print ("on peut commencer le projet 01 prix mystère")

import random

"""
Ce programme est un jeu "Prix Mystère".
Le joueur doit deviner le prix caché.
Le programme donnera des indices "plus haut" ou "plus bas".
"""
print ( " Bienvenue dqns le jeu du prix mystere")
print ( " le but du jeu est de deviner un nombre entre 1 et 100 " )

# random permet de generer les nombres
# je cree une variable prix et j utilise lq fonction random pour generer un nombre aleatoirement et randint pour aue ce nombre soit un entier

prix = random.randint(1, 100)
trouve = True
tentatives = 0
while trouve:
# il faut aue l utilisqteur entre le nombre, je cree une fonction guess
    guess =  int ( input ( " entrez votre proposition: ")) # car je souhaite aue l utilisateur retourne un entier
    tentatives += 1
    if guess < prix:
        print ( " c'est plus" )
    elif guess > prix:
        print (" c'est moins")
    else:
        print ( " Bravo, vous avez trouve le prix mystere ", prix, "en", tentatives, "tentatives")
        trouve = False






