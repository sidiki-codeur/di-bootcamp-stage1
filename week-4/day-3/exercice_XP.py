#exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

liste=dict(zip(keys,values))
print(liste)


#------------------------------------------------------------------
#exercice 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total=0
for ind in family:
    if family[ind] < 3:
        print("l'entree est gratuit pour {ind}")
    elif family[ind] < 12:
        print(f"{ind} paye la somme de 10$")
        total+=10
    else:
        print(f"{ind} paye la somme de 15$")
        total+=15

print(f"la famille doit paye au total {total}$")

#---------------------------------------------------------------
#Bonus
family = {}

while True:
    nom=input("entrer le nom d'un memebre de la famille :")
    age=int(input("entrer aussi son age :"))
    family[nom]=age
    rep=input("voulez-vous ajouter quelqu'un d'autre ? O(oui) / N(non)")
    if rep=="n":
        break
total=0
for ind in family:
    if family[ind] < 3:
        print(f"l'entree est gratuit pour {ind}")
    elif family[ind] < 12:
        print(f"{ind} paye la somme de 10$")
        total+=10
    else:
        print(f"{ind} paye la somme de 15$")
        total+=15

print(f"la famille doit paye au total {total}$")


#exercice 3
#2
brand={
    "name":"Zara",
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes":["men","women","children","home"], 
    "international_competitors":["Gap","H&M","Benetton"], 
    "number_stores": 7000, 
    "major_color": {
        "France":"blue", 
        "Spain":"red",
        "US": ["pink","green"]
    }
}

#3
brand["number_stores"]=2

#4
print("les clients de zara sont :",brand["type_of_clothes"])

#5
brand["country_creation"]="Spain"

#6
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#7
del brand["creation_date"]

#8
print("dernier concurrent internationnal :",brand["international_competitors"][-1])

#9
print(" les principales couleurs us :",brand["major_color"]["US"])

#10
print("nombre de clee :",len(brand))

#11
print("les clees :" ,brand.keys())

#12
more_on_zara={"creation_date": 1975 ,"number_stores": 10000}

#13
brand.update(more_on_zara)

#14
print("nombre de magasin :",brand["number_stores"])
#l'interpreteur affichera la recente va leur de "number_stores" soit 100000


#exercice 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#1
disney_users_A={}
i=0
for elem in users:
    disney_users_A[elem]=i
    i+=1
print(disney_users_A)

#2
disney_users_B={}
i=0
for elem in users:
    disney_users_B[i]=elem
    i+=1
print(disney_users_B)

#3
disney_users_C={}
i=0
users.sort()
for elem in users:
    disney_users_C[elem]=i
    i+=1

print(disney_users_C)

#4-1
disney_users_A1={}
i=0
for elem in users:
    if "i" in elem:
        disney_users_A1[elem]=i
        i+=1
print(disney_users_A1)

#4-2
disney_users_A2={}
i=0
for elem in users:
    if elem[0]=="M" or elem[0]=="P":
        disney_users_A2[elem]=i
        i+=1
print(disney_users_A2)