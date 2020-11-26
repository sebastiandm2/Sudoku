from random import seed
from random import randint

def printBoard(board): #prints board of dimension 9x9
    for i in range(9):
        for j in range(9):
            if(j % 3 == 0 and j > 0): #prints vertical line to make a sub grid of dimension 3x3
                print("|"),
            print(board[i][j]),
        print("")
        if(i == 2 or i == 5): #prints horizantal line to make a sub grid of dimension 3x3
            for _ in range(11):
                print("-"),
            print("")

def checkQuadrant(board, row, col, num):
    if(row >= 0 and row <= 2 and col >= 0 and col <= 2): #top left quadrant
        x = (0, 0) #top left of quadrant
    if(row >= 0 and row <= 2 and col >= 3 and col <= 5): #top middle quadrant
        x = (0, 3) #top left of quadrant
    if(row >= 0 and row <= 2 and col >= 6 and col <= 8): #top right quadrant
        x = (0, 6) #top left of quadrant
    if(row >= 3 and row <= 5 and col >= 0 and col <= 2): #middle left quadrant
        x = (3, 0) #top left of quadrant
    if(row >= 3 and row <= 5 and col >= 3 and col <= 5): #middle middle quadrant
        x = (3, 3) #top left of quadrant
    if(row >= 3 and row <= 5 and col >= 6 and col <= 8): #middle right quadrant
        x = (3, 6) #top left of quadrant
    if(row >= 6 and row <= 8 and col >= 0 and col <= 2): #middle left quadrant
        x = (6, 0) #top left of quadrant
    if(row >= 6 and row <= 8 and col >= 3 and col <= 5): #middle middle quadrant
        x = (6, 3) #top left of quadrant
    if(row >= 6 and row <= 8 and col >= 6 and col <= 8): #middle right quadrant
        x = (6, 6) #top left of quadrant

    for i in range(3): #checking quadrant to see if num is repeated
        for j in range(3):
            r = x[0] + i
            c = x[1] + j
            if(board[r][c] == num and r != row and c != col):
                return True #value is repeated
    
    return False
    

def isRepeat(board, empty, num):
    row = empty[0]
    col = empty[1]
    for i in range(9): #checking if num is repeated in row
        if(board[row][i] == num):
            return True
    for i in range(9): #checking if num is repeated in col
        if(board[i][col] == num):
            return True
    if(checkQuadrant(board, row, col, num)): #checking if num is repeated in the quadrant
        return True

    return False

def findEmpty(board): #finds next empty slot
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0): #if slot is 0 => then it is empty so we return this position
                return (i, j)
    return (-1, -1) #return invalid index if all are filled

def buildBoard(board): #builds board given a start at position (0, 0)
    if(board[8][8] != 0): #checks if board is full
        return True
    
    #BACKTRACKING
    row, col = findEmpty(board) #find empty slot
    for i in range(1, 10): #find first number that works
        if(not isRepeat(board, (row, col), i)): #checks if number is repeated
            board[row][col] = i #if not repeated => put num in empty slot

            if(buildBoard(board)): #recursively build
                return True
            board[row][col] = 0 #reset our position if we backtracked

    return False


print("Welcome to Sudoku Player! Would you like to play a game or watch an automated game? ") #print menu
userInput = input("Select 1 to play \nSelect 0 to watch \n")
play = True

board = [[0]*9 for i in range(9)]
board[0][0] = randint(1, 9)
buildBoard(board)
while(play):
    printBoard(board)
    num = input("Enter the number you want to play (enter -1 to exit): ")
    if(num == -1):
        break
    if(num > 9 or num < 1):
        print("Not a valid number! Try again.")
        continue

    y = input("Enter row: ")
    x = input("Enter column: ")
    if(x > 9 or x < 1 or y > 9 or y < 1):
        print("Not a valid index! Try again.")
        continue

    board[y-1][x-1] = num

    #play = False
