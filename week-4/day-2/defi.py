#defi-1
number=int(input("entrer un nombre  : "))
length=int(input("entrer une taille : "))

print(f"number: {number} - length {length} ➞ [",end="")
for i in range(1,length+1):
    print(number*i,end="")
    if(i!=length):
        print('',end=" ,")
print("]")


#defi-2
chaine=input("entrer une chaine de caractere : ")
resultat=chaine
print("avant : ",resultat)
for i in chaine:
    while i+i in resultat:
        resultat=resultat.replace(i+i,i)

print("apres : ",resultat)
