from os import system
from random import uniform


#Exercice 1
print("exercice 1")

def display_message():
    print("nous avons appris a manipuler les fonctions")

display_message()
system("pause")


#------------------------------------------------------------------
#Exercice 2
print("exercice 2")

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("Tribalic")
system("pause")



#------------------------------------------------------------------
#Exercice 3
def describe_city(city,country="Burkina Faso"):
    print(f"{city} est au {country}")

describe_city("Ouagadougou")
system("pause")



#------------------------------------------------------------------
#Exercice 4
def aleatoire(number):
    x=choice(range(1,101))
    if x == number:
        print("you win")
    else:
        print("you loose")
        print(f"you give {number} but the mystic number was {x}")

number=int(input("game : devine a mystic number between 1 et 100 :"))
aleatoire(number)
system("pause")



#------------------------------------------------------------------
#Exercice 5
def make_shirt(size="XXXL",text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("L","no code , no life")

make_shirt()

make_shirt("M")

make_shirt("L","peace and love")
system("pause")

#bonus
print("bonus")

def make_shirt_bonus(**params):
    print(f"The size of the shirt is {params['size']} and the text is {params['text']}")

make_shirt_bonus(size="L",text="peace and love")
system("pause")

#------------------------------------------------------------------
#Exercice 6
print("execice 6")

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians_liste):
    for magician in magicians_liste:
        print(magician)

def make_great(magicians_liste):
    for i in range(len(magicians_liste)):
        magicians_liste[i]="the Great "+magicians_liste[i]
    return magicians_liste


show_magicians(magician_names)
magician_names=make_great(magician_names)
show_magicians(magician_names)


#------------------------------------------------------------------
#Exercice 7
print("execice 7")


def get_random_temp(season):
    if season.lower() == "winter":
        return uniform(-10,16)
    elif season.lower() == "summer":
        return uniform(16,24)
    elif season.lower() == "spring":
        return uniform(4,31)
    elif season.lower() == "autumn":
        return uniform(31,40)
    else:
        print("error")
        return -111111111


def main():
    season=input("enter the current season : ")
    temperature=get_random_temp(season)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today ")
    elif temperature >=0 and temperature < 16:
        print("Quite chilly! Don’t forget your coat")
    elif temperature >=16 and temperature < 24:
        print("lol ! a little cold")
    elif temperature >=24 and temperature < 32:
        print("good weather is coming")
    else:
        print("heat, heat and heat !")

main()