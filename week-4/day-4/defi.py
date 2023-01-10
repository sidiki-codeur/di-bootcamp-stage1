from string import ascii_letters

texte=[ "7i_",
        "Ts.",
        "h% ",
        "i i",
        "sMx",
        "$a3",
        "#t%",
        "^r!" ]

code=""

for i in range(3):
    for j in range(len(texte)):
        code+=texte[j][i]
        
e="x"
resultat=""

for i in code:
    if i in ascii_letters:
        if e not in ascii_letters:
            resultat+=" "
        resultat+=i
    e=i

print(resultat)