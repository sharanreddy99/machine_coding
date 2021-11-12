# packages
from random import randrange

# constants
LEFT = 0
RIGHT = 1
TOP = 2
BOTTOM = 3

# variables
board = []
rows = 0
cols = 0

def fileWrite(fileName,mode,value):
    fp = open(fileName,mode)
    fp.write(value)
    fp.close()

def initializeBoard():
    
    fileWrite('result.txt','w','Board Moves\n-----------\n')   
    try:
        readInput()
        addRandomTile(2)
        printBoard(None)

        while isEmptyTileExists():
            if checkGameWon():
                print('\nCongratulations! You won')
                return
            
            direction = getDirection()
            moveAllTiles(direction)
            addRandomTile(1)
            printBoard(direction)
    except Exception as e:
        print(e)

def readInput():
        global board,rows,cols
        rows = int(input("\nEnter no of rows: "))
        cols = int(input("\nEnter no of cols: "))
        board = [['-' for i in range(cols)] for j in range(rows)]

def getDirection():
    while True:
        direction = int(input("\nEnter direction to move the tiles: \n Choose\n ------\n (0) to move left\n (1) to move right\n (2) to move to top\n (3) to move to bottom\n Your Input:  "))
        if direction in (TOP,BOTTOM,LEFT,RIGHT):
            if canMoveTiles(direction):
                return direction
            else:
                print('\nDirection not allowed. Please choose another direction.')
        else:
            print('\nInvalid direction chosen. Please try again')
        
def canMoveTiles(direction):
    global board, rows, cols
    if direction == TOP:
        for colIdx in range(cols):
            for rowIdx in range(rows-1):
                if board[rowIdx][colIdx] == '-' and board[rowIdx+1][colIdx] == '-':
                    continue
                elif board[rowIdx][colIdx] == '-' and board[rowIdx+1][colIdx] != '-':
                    return True
                elif board[rowIdx][colIdx] == board[rowIdx+1][colIdx] and board[rowIdx][colIdx] != '-':
                    return True
    elif direction == BOTTOM:
        for colIdx in range(cols):
            for rowIdx in range(rows-1):
                if board[rowIdx][colIdx] == '-' and board[rowIdx+1][colIdx] == '-':
                    continue
                elif board[rowIdx][colIdx] != '-' and board[rowIdx+1][colIdx] == '-':
                    return True
                elif board[rowIdx][colIdx] == board[rowIdx+1][colIdx] and board[rowIdx][colIdx] != '-':
                    return True
    
    elif direction == LEFT:
         for rowIdx in range(rows):
            for colIdx in range(cols-1):
                if board[rowIdx][colIdx] == '-' and board[rowIdx][colIdx+1] == '-':
                    continue
                elif board[rowIdx][colIdx] == '-' and board[rowIdx][colIdx+1] != '-':
                    return True
                elif board[rowIdx][colIdx] == board[rowIdx][colIdx+1] and board[rowIdx][colIdx] != '-':
                    return True
    else:
        for rowIdx in range(rows):
            for colIdx in range(cols-1):
                if board[rowIdx][colIdx] == '-' and board[rowIdx][colIdx+1] == '-':
                    continue
                elif board[rowIdx][colIdx] != '-' and board[rowIdx][colIdx+1] == '-':
                    return True
                elif board[rowIdx][colIdx] == board[rowIdx][colIdx+1] and board[rowIdx][colIdx] != '-':
                    return True
    return False

def moveAllTiles(direction):
    if direction == TOP:
        moveTilesTop()
    elif direction == BOTTOM:
        moveTilesBottom()
    elif direction == LEFT:
        moveTilesLeft()
    else:
        moveTilesRight()

def moveTilesTop():
    global rows, cols, board
    colIdx = cols - 1
    while colIdx >= 0:
        rowIdx = 0
        while rowIdx < rows - 1:
            if board[rowIdx][colIdx] == board[rowIdx+1][colIdx]:
                if board[rowIdx][colIdx] == '-':
                    rowIdx += 2
                    continue

                board[rowIdx][colIdx] += board[rowIdx+1][colIdx]
                board[rowIdx+1][colIdx] = '-'
                rowIdx += 1    
            rowIdx += 1
        shiftTilesTop(colIdx)
        colIdx -= 1

def moveTilesBottom():
    global rows, cols, board
    colIdx = cols - 1
    while colIdx >= 0:
        rowIdx = rows - 1
        while rowIdx > 0:
            if board[rowIdx][colIdx] == board[rowIdx-1][colIdx]:
                if board[rowIdx][colIdx] == '-':
                    rowIdx -= 2
                    continue

                board[rowIdx][colIdx] += board[rowIdx-1][colIdx]
                board[rowIdx-1][colIdx] = '-'
                rowIdx -= 1    
            rowIdx -= 1
        shiftTilesBottom(colIdx)
        colIdx -= 1

def moveTilesLeft():
    global rows, cols, board
    rowIdx = rows - 1
    while rowIdx >= 0:
        colIdx = 0
        while colIdx < cols - 1:
            if board[rowIdx][colIdx] == board[rowIdx][colIdx+1]:
                if board[rowIdx][colIdx] == '-':
                    colIdx += 2
                    continue

                board[rowIdx][colIdx] += board[rowIdx][colIdx+1]
                board[rowIdx][colIdx+1] = '-'
                colIdx += 1    
            colIdx += 1
        shiftTilesLeft(rowIdx)
        rowIdx -= 1

def moveTilesRight():
    global rows, cols, board
    rowIdx = rows - 1
    while rowIdx >= 0:
        colIdx = cols - 1
        while colIdx > 0:
            if board[rowIdx][colIdx] == board[rowIdx][colIdx-1]:
                if board[rowIdx][colIdx] == '-':
                    colIdx -= 2
                    continue

                board[rowIdx][colIdx] += board[rowIdx][colIdx-1]
                board[rowIdx][colIdx-1] = '-'
                colIdx -= 1    
            colIdx -= 1
        shiftTilesRight(rowIdx)
        rowIdx -= 1

def shiftTilesTop(colIdx):
    global board, rows
    while True:
        isMoved = False
        for idx in range(rows-1):
            if board[idx][colIdx] == '-' and  board[idx][colIdx] == board[idx+1][colIdx]:
                continue
            
            if board[idx][colIdx] == '-':
                isMoved = True
                board[idx][colIdx] = board[idx+1][colIdx]
                board[idx+1][colIdx] = '-'

        if isMoved == False:
            break

def shiftTilesBottom(colIdx):
    global board, rows
    while True:
        isMoved = False
        for idx in range(rows-1,0,-1):
            if board[idx][colIdx] == '-' and board[idx][colIdx] == board[idx-1][colIdx]:
                continue

            if board[idx][colIdx] == '-':
                isMoved = True
                board[idx][colIdx] = board[idx-1][colIdx]
                board[idx-1][colIdx] = '-'
            
        if isMoved == False:
            break

def shiftTilesLeft(rowIdx):
    global board, cols
    while True:
        isMoved = False
        for idx in range(cols-1):
            if board[rowIdx][idx] == '-' and  board[rowIdx][idx] == board[rowIdx][idx+1]:
                continue
            
            
            if board[rowIdx][idx] == '-':
                isMoved = True
                board[rowIdx][idx] = board[rowIdx][idx+1]
                board[rowIdx][idx+1] = '-'
             
        if isMoved == False:
            break

def shiftTilesRight(rowIdx):
    global board, cols
    while True:
        isMoved = False
        for idx in range(cols-1, 0, -1):
            if board[rowIdx][idx] == '-' and  board[rowIdx][idx] == board[rowIdx][idx-1]:
                continue
            
            if board[rowIdx][idx] == '-':
                isMoved = True
                board[rowIdx][idx] = board[rowIdx][idx-1]
                board[rowIdx][idx-1] = '-'
        
        if isMoved == False:
                break

def isEmptyTileExists():
    global board
    for row in board:
        for tile in row:
            if tile == '-':
                return True
    return False

def setEmptyTile(rowIdx, colIdx):
    global board
    board[rowIdx][colIdx] = '-'

def addRandomTile(no_of_tiles):
    global board, rows, cols
    
    while no_of_tiles > 0:
        row_loc = randrange(rows)
        col_loc = randrange(cols)
        if board[row_loc][col_loc] == '-':
            board[row_loc][col_loc] = 2
            no_of_tiles -=1
        else:
            continue

def checkGameWon():
    global board
    for row in board:
        for tile in row:
            if tile == 2048:
                return True
    return False

def printBoard(direction):
    directionMap = {0: 'LEFT', 1: 'RIGHT', 2: 'TOP', 3:'BOTTOM',None: 'Initial'}

    print('\n Board:\n ------\n')
    print('Direction: '+directionMap[direction]+'\n')
    global board
    for row in board:
        for tile in row:
            print(tile,end=' ')
        print()
    print()

    global fp
    rowStr = 'Direction: '+directionMap[direction]+'\n'
    for row in board:
        for tile in row:
            rowStr += str(tile) + ' ' 
        rowStr += '\n'
    rowStr += '\n\n----------------------\n\n'

    fileWrite('result.txt','a',rowStr)
initializeBoard()