chaine=input("entrer une chaine de caracteres : ")
if len(chaine)<10:
    print("chaîne pas assez longue")
else:
    print("chaîne trop longue")

print(f"premier caractere : {chaine[0]} dernier caractere : {chaine[-1]}")

afficher=""
for i in chaine:
    afficher+=i
    print(afficher)