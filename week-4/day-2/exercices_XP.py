#exercice 1
my_fav_numbers={7536,7710,7197}

my_fav_numbers.add(6021)
my_fav_numbers.add(6453)

dernierElement=None
for i in my_fav_numbers:
    dernierElement=i

my_fav_numbers.remove(dernierElement)

friend_fav_numbers={7210,5676,7546}

our_fav_numbers=set()
our_fav_numbers.update(my_fav_numbers,friend_fav_numbers)

print(our_fav_numbers)


#---------------------------------------------------------------------------
#exercice 2
"""
Non il n'est pas possible d'ajouter ou de retirer des elements a un tuple
"""


#---------------------------------------------------------------------------
#exercice 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")

nb_pommes=basket.count("Apples")
print(f"{nb_pommes} Apples in the basket")
basket.clear()

print(basket)


#---------------------------------------------------------------------------
#exercice 4
"""
1)- float est un type de variable, comme int, short ou double.
Ce type est utilisé pour stocker des nombres à virgule flottante,
désignés en anglais par l'expression floating point numbers.

  - un entier int est stocké sur 4 octets (32 bits) tandis qu'un
nombre flottant float est stocké sur 8 octets (64 bits).

2)Non,nous ne pouvons pas pensez à une autre façon de générer une
séquence de flottants.

3)
L=[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

"""

#---------------------------------------------------------------------------
#exercice 5
l=range(1,21)
print("tous les nombres :")
for i in l:
    print(i)

print("tous les nombres avec des indexes paires :")
for i in range(len(l)):
    if i%2==0 and i!=0:
        print(l[i])


#---------------------------------------------------------------------------
#exercice 6
my_name="sidiki"
username=""

while my_name!=username:
    username=input("entrer un nom :")


#---------------------------------------------------------------------------
#exercice 7
fruits_favoris=input("entrer vos fruits favories en separant par des espaces :")
fruits_favoris=fruits_favoris.split(" ")
fruit=input("entrer le nom d'un fruit : ")
if fruit in fruits_favoris:
    print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
else:
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies")


#---------------------------------------------------------------------------
#exercice 8
garnitures=[]
garn=""
while garn!="quitter":
    garn=input("entrer une garnitures a ajouter :")
    print(f"{} sera ajoute a vote pizza ")
    garnitures.append(garn)

print("liste des garnitures : ")
for garniture in garnitures:
    print(garniture)

total=10+2.5*len(garnitures)
print(f"Total de la commande : {}",total)


#---------------------------------------------------------------------------
#exercice 9
reponse="o"
total=0
while reponse=="o":
    age=int(input("entrer l'age de la personne :"))
    if age < 3:
        prix_ticket=0
    elif age>=3 and age<=12:
        prix_ticket=10
    else:
        prix_ticket=15
    total+=prix_ticket

    reponse=input("voulez-vous payer un autre ticket ? oui(o) non(n) ::")

print(f"Total a payer : {total}")

liste=["ali","moussa","karim","saly","fati"]
for nom in liste:
    age=int(input(f"{nom} :: ton age : "))
    if age < 15 or age > 21:
        liste.remove(nom)
print(liste)


#---------------------------------------------------------------------------
#exercice 10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]
while len(sandwich_orders):
    print("sandwich prepare     : ",sandwich_orders)
    print("sandwich non prepare : ",finished_sandwiches)
    sandwich=input("entrer le nom du sandwich prepare")
    if sandwich in sandwich_orders:
        sandwich_orders.remove(sandwich)
        finished_sandwiches.append(sandwich)
        print("sandwich ajoute avec succes !")
    else:
        print("ce sandwich n'est pas sur la liste des sandwich a prepare")

print("I made your tuna sandwich")


#---------------------------------------------------------------------------
#exercice 11
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
print("la charcuterie n'a plus de pastrami")
for sandwich in sandwich_orders:
    if sandwich=="Pastrami sandwich":
        sandwich_orders.remove(sandwich)

finished_sandwiches=sandwich_orders