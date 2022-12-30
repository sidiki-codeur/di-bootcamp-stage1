#defi 1
mot=input("entrer un mot :")
dico={}
for i in range(len(mot)):
    if mot[i] not in dico:
        dico[mot[i]]=[]
    dico[mot[i]].append(i)
print(dico)


#defi 2
items_purchase={
    "sac":5000,
    "nano":90000,
    "pc hp":20000,
    "apple":600000,
    "sirius":400000
}

wallet=100000

good_items=[]

for i in items_purchase:
    if items_purchase[i] <=wallet:
        good_items.append(i)

if len(good_items)==0:
    print("Rien")
else:
    print(good_items)