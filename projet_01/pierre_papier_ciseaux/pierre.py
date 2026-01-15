# je definis les fonctions pour les choix 
import random

def choix_utilisateur():
    """cette fonction va permettre a l utisateur de choisir"""
    joueur = input ("pierre\n papier\n ciseaux\n")
    return (joueur)

def choix_ordi():
    # fonction pour permettre a l ordinqteur de choisir aleatoirement un choix
    ordi = random.choice(["pierre", "papier", "ciseaux"]).lower()  # .lower() pour s'assurer que le choix est en minuscules
    return(ordi)

# les conditions pour gqgner ou perdre

a = choix_utilisateur()
b = choix_ordi()

print("Ordinateur a choisi :", b)
print("Vous avez choisi :", a)
# print(b)
if a == "pierre" and b == "ciseaux":
    print("Vous avez gagne.")
elif a == "pierre" and b == "papier":
    print("Vous avez perdu.")
elif a == "pierre" and b == "pierre":
    print("Egalite.")
 
if a == "papier" and b == "pierre":
    print("Vous avez gagne.")
elif a == "papier" and b == "ciseaux":
    print("Vous avez perdu.")
elif a == "papier" and b == "papier":
    print("Egalite.")
 
if a == "ciseaux" and b == "papier":
    print("Vous avez gagne.")
elif a == "ciseaux" and b == "pierre":
    print("Vous avez perdu.")
elif a == "ciseaux" and b == "ciseaux":
    print("Egalite.")


