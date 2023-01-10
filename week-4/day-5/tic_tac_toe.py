def display_board(cadre):
    print("tic tac toe")

    print("-------------")
    for i in range(3):
        print("|",end="")
        for j in range(3):
            print(f" {cadre[i][j]}",end=" |")
        print("\n-------------")

def player_input(cadre,joueur):
    print(f"JOUEUR {joueur}")
    row=int(input("enter the row : "))
    column=int(input("enter the column : "))

    while cadre[row-1][column-1] != " ":
        print("this position is not free , try an other position !")
        row=int(input("enter the row : "))
        column=int(input("enter the column : "))
    
    cadre[row-1][column-1]="X" if joueur==1 else "O"

    return cadre


def check_win(cadre):
    winner=""
    for i in range(3):
        if cadre[i][0]==cadre[i][1] and cadre[i][1]==cadre[i][2]:
            winner+=cadre[i][0]
        if cadre[0][i]==cadre[1][i] and cadre[1][i]==cadre[2][i]:
            winner+=cadre[0][i]

    if cadre[0][0]==cadre[1][1] and cadre[1][1]==cadre[2][2]:
        winner+=cadre[0][0]
    
    if cadre[2][0]==cadre[1][1] and cadre[1][1]==cadre[0][2]:
        winner+=cadre[0][i]
    
    while " " in winner:
        winner=winner.replace(" ","")
    
    return winner

def play():
    i=0
    cadre=[]
    for i in range(3):
        cadre.append([])
        for j in range(3):
            cadre[i].append(" ")

    while True:
        joueur=i%2+1
        display_board(cadre)
        cadre=player_input(cadre,joueur)
        winner=check_win(cadre)
        if len(winner) > 0:
            if winner=="X":
                print("JOUEUR 1 GAGNE")
            elif winner=="O":
                print("JOUEUR 2 GAGNE")
            else:
                print("egalite")
            break
        i+=1

play()