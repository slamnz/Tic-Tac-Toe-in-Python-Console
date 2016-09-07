"""TO-DO LIST
    Write win condition. How to exclude " "
"""

from random import randint

#FUNCTIONS

def initialise():
    grid = []
    for i in range(3):
        grid.insert(i, ["[ ]"] * 3)
    return grid

def print_grid(grid):
    print("[ ][1][2][3]")
    for i in range(len(grid)):
        print ("[" + str(i+1) + "]" + "".join(grid[i]))
    print("")

def mark(grid,symbol,x,y):
    x = int(x)
    y = int(y)
    grid[x][y] = "[" + symbol + "]"
        
def symbolIsValid(symbol):
    if(not (len(symbol) == 1 or symbol == " ")):
        return False
    else:
        return True

def inputIsValid(n):
    try:
        if(int(n) in range(1,4)):
            return True
        else:
            return False
    except Exception:

        return False

def isEmpty(grid, x, y):
    return grid[x][y] == "[ ]"

def win(grid):

    rowOne = not isEmpty(grid, 0, 0) and grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]
    rowTwo = not isEmpty(grid, 1, 0) and grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]
    rowThree = not isEmpty(grid, 2, 0) and grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]
    columnOne = not isEmpty(grid, 0, 0) and grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]
    columnTwo = not isEmpty(grid, 0, 1) and grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]
    columnThree = not isEmpty(grid, 0, 2) and grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]
    diagonalOne = not isEmpty(grid,0,0) and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]
    diagonalTwo = not isEmpty(grid,0,2) and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]

    if rowOne or rowTwo or rowThree or columnOne or columnTwo or columnThree or diagonalOne or diagonalTwo:
        return True
    else:
        return False

def consoleDivider():
    print("=================================================")

#SELECT YOUR SYMBOL

consoleDivider()
print("Welcome to Tic Tac Toe")
print("Sunny Lam / 30 August 2016")
consoleDivider()
symbol = str(input("Choose your symbol: "))
consoleDivider()

while(not symbolIsValid(symbol)):
    print("The symbol you chose is invalid.")
    symbol = str(input("Please choose another your symbol: "))

#OPPONENT SELECTS THEIR SYMBOL

opponent = ""

if(not symbol == "O"):
    opponent = "O"
else:
    opponent = "X"

print("Your opponent's symbol is: " + opponent)

#START GAME

round = 0
grid = initialise()
isFinished = False

while(not isFinished):
    
    if(win(grid)):
        print("Someone wins")
        new_game = input("New game? Yes / No")
        if new_game == "Yes":
            isFinished = False
            round = 0
            print("NEW GAME")
        elif new_game == "No":
            isFinished = True
        else:
            print("Stop trying to break the program. Game terminated.")
            break
    
    round += 1
    consoleDivider()
    print("\nROUND " + str(round))
    print_grid(grid)

    print("YOUR TURN")

    #PLAYER'S INPUT
    
    while(True):
        
        #MARK A ROW
        
        guess_row = input("Mark the row: ")

        ##CHECK IF ROW INPUT IS VALID

        while(not inputIsValid(guess_row)):
            print("Invalid input for row. Enter again.")
            guess_row = input("Mark the row: ")

        #MARK A COLUMN
        guess_col = input("Mark the column: ")

        ##CHECK IF COLUMN INPUT IS VALID
        
        while(not inputIsValid(guess_col)):
            print("Invalid input for column. Enter again.")
            guess_col = input("Mark the column: ")

        #CONFIRM MARKED COLUMN
            
        guess_row = int(guess_row) - 1
        guess_col = int(guess_col) - 1

            
        if isEmpty(grid, guess_row, guess_col):
            mark(grid,symbol,guess_row,guess_col)
            print("\nYou have marked row %d, column %d" % (guess_row + 1, guess_row + 1))
            print_grid(grid)
            break
            
        else:
            print("This position has already been marked. Choose another.")
            
    #OPPONENT'S TURN
    consoleDivider()
    print("Opponent's Turn")
    while(True):
        guess_row = randint(0,2)
        guess_col = randint(0,2)
        if isEmpty(grid,guess_row,guess_col):
            mark(grid,opponent,guess_row,guess_col)
            print_grid(grid)
            break
        
        
    

