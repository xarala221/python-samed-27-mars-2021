# nombre1 = 20
# nombre2 = 10
# multiplication = nombre1 * nombre2
# division = nombre1 / nombre2
# division_entier = nombre1 // nombre2
# soustraction = nombre1 - nombre2
# addition = nombre1 + nombre2
# exponent = nombre1 ** 2

"""
Excercice: Demandez l'utilisateur de donner les deux nombres en utilisant les fonctions.
Afficher un message d'erreur si l'utiliateur met 0

"""
# print("multplication ", multiplication)
# print("division ", division)
# print("division_entier ", division_entier)
# print("soustraction ", soustraction)
# print("addition ", addition)
# print("exponent ", exponent)

# built-in functins
# nom = input("Votre nom svp? ")

# mot_cle nom_de_la_fonction():
# corps
# def afficher_nom():
#     print("Talla Kane")

# afficher_nom()

# def addition(nombre1, nombre2):
#     resultat = nombre1 + nombre2
#     print(resultat)

# addition(20, 5)

# Strctures de donnees

# mon_tableau = [2, 3, "Diop", "Ndiaye", "Khady", "Fatou"]
# print("Elment ", mon_tableau)
# mon_tableau.append("Talla")
# print("Elment ", mon_tableau)
# mon_tableau.insert(2, "Bary")
# print("Elment ", mon_tableau)
# mon_tableau.pop()
# print("Elment ", mon_tableau)
# mon_tableau.remove(2)
# print("Elment ", mon_tableau)
# del mon_tableau [2]
# print("Elment ", mon_tableau)

# tableau_1 = [3, 4, "Mareme"]
# tableau_2 = [5, "Khady", "Awa"]

# tableaux = [tableau_1 , tableau_2]
# quel est le resulat de tableaux[0][1]
# sort_tableau = [3,8, 1, 9, 4]
# sort_tableau[0] = 7
# sort_tableau.sort()
# print("tableaux ", sort_tableau[0:3])

# Boucle
# message = "Je t'aime Awa"
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
# print(message)
# for nombre in range(10):
#     print(message)

# sort_tableau = [3,8, 1, 9, 4]
# for nombre in sort_tableau:
#     print(nombre)

# comprehension_list = [element for element in iterable]
# nombre_expo = [nombre ** 2 for nombre in sort_tableau]
# print(nombre_expo)

# mon_tuple = (1, 3, 4)
# # Challenge 2 comment changer une valeur dans un tuple

# dict_wolof = {"jollasu": "Telephone", "aajar": "presenter"}

# for mot, signification in dict_wolof.items():
#     print(mot, signification)

"""
= assigner
== comparer
!= not egal
< inferieur
> superieur
<=
>=
"""
# age_saawaay = 25
# age_awa = 15
# nationalite = "senegalaise"

# if age_saawaay == age_awa or age_awa > age_saawaay:
#     print("Maa ban")
# elif age_saawaay > age_awa and nationalite == "senegalaise":
#     print("Nangu naa")
# else:
#     print("Awma tontu")


# while age_awa < 18:
#     print("Alalou procureur")
#     age_awa += 1
#     if age_awa == 17:
#         print("At moo si des")
#         break

class Voiture:

    def __init__(self, model):
        self.model = model

    def daw(self):
        return "Voiture baa ngi daw"


class Vehicule(Voiture):

    def daw(self):
        return "Vehicule baa ngi daw"


# voiture1 = Voiture("Tesla X")
# vehicule1 = Vehicule("Toyota")
# print(voiture1.model)
# print(voiture1.daw())

# print(vehicule1.model)
# print(vehicule1.daw())


# Exception and error handling
nombre1 = int(input("Nombre 1: "))

nombre2 = int(input("Nombre 2: "))

try:
    print(nombre1 / nombre2)
except ZeroDivisionError:
    print("Division par zero, n'est pas permi")
