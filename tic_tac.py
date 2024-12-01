from art import *;

winning_combinations = [
    # Rows
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    
    # Columns
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    
    # Diagonals
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

x=True
l=[["_","_","_"],["_","_","_"],["_","_","_"]]
def display():
    for i in range(0,3):
        print("|",end="")
        for j in range(0,3):
            print(l[i][j],"|",end="")
        print()

def checkWin():
    for combination in winning_combinations:
        # Get the symbols in the winning positions
        symbols = [l[i[0]][i[1]] for i in combination]
        
        if symbols[0] != "_" and symbols[0] == symbols[1] == symbols[2]:
            return symbols[0]  
    
    return None  
def checkDraw():
    for row in l:
        for cell in row:
            if(cell=="_"):
                return False
    return True

while True:
    display()
    if(x):
        print("\nX's turn")
        r=int(input("Enter row number between 0 and 2: "))
        c=int(input("Enter column number between 0 and 2: "))
        if(r>2 or r<0) or (c>2 or c<0) or l[r][c]!='_':
            print("Wrong row or col number")
            continue
        l[r][c]='X'
        x=False
    else:
        print("\nO's turn")
        r=int(input("Enter row number between 0 and 2: "))
        c=int(input("Enter column number between 0 and 2: "))
        if(r>2 or r<0) or (c>2 or c<0) or l[r][c]!='_':
            print("Wrong row or col number")
            continue
        l[r][c]='O'
        x=True
    t=checkWin()
    if t != None:
        display()
        print(text2art(f"{t}  is  winner"))
        break
    if checkDraw()==True:
        display()
        print(text2art("Draw :("))
        break
    
        


