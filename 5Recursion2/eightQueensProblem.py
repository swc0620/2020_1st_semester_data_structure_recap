BOARD_SIZE = int(input())
board = [[0 for i in range(BOARD_SIZE + 2)] for j in range(BOARD_SIZE + 2)]

def isUnderAttack(row, col):
    for i in range(col):
        if board[row][i] == 1:
            return True
    
    for j in range(row):
        if board[j][col] == 1:
            return True

    for k in range(1, min(row, col)):
        if board[row - k][col - k] == 1:
            return True

    for l in range(1, min(BOARD_SIZE + 1 - row, col)):
        if board[row + l][col - l] == 1:
            return True
    
    return False

def removeQueen(row, col):
    board[row][col] = 0

def setQueen(row, col):
    board[row][col] = 1

def placeQueens(col):
    if col > BOARD_SIZE:
        return True
    else:
        queenplaced = False
        row = 1
        while not queenplaced and row <= BOARD_SIZE:
            if isUnderAttack(row, col):
                row += 1
            else:
                setQueen(row, col)
                queenplaced = placeQueens(col+1)
                if not queenplaced:
                    removeQueen(row, col)
                    row += 1
        return queenplaced

placeQueens(1)
for i in range(BOARD_SIZE + 2):
    for j in range(BOARD_SIZE + 2):
        if board[i][j] == 1:
            print(j)