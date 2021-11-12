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

def setCustomBoard():
    global board,rows,cols
    rows = 2
    cols = 2
    board = [['-' for i in range(cols)] for j in range(rows)]
    arr = [(0,0,2),(0,1,2),(1,0,4),(1,1,4)]
    for r in arr:
        if r[0] == 'X':
            for x in range(rows):
                board[x][r[1]] = r[2]
        elif r[1] == 'X':
            for y in range(cols):
                board[r[0]][y] = r[2]
        elif r[0] == 'X' and r[1] == 'X':
            for x in range(rows):
                for y in range(cols):
                    board[x][y] = r[2]
        else:
            board[r[0]][r[1]] = r[2]

def initializeBoard(isCustomBoard = False):
    
    fileWrite('result.txt','w','Board Moves\n-----------\n')   
    try:
        if isCustomBoard == False:
            readInput()
            addRandomTile(2)
        else:
            setCustomBoard()
        printBoard(None)

        while isEmptyTileExists() or canMergeAny():
            if checkGameWon():
                print('\nCongratulations! You won')
                return
            
            direction = getDirection()
            moveAllTiles(direction)
            addRandomTile(1)
            printBoard(direction)
        print('\nGame Over')
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
        
def areTilesMovable(row_step1,col_step1,row_step2,col_step2,rows,cols,isInvert=False):
    for colIdx in range(cols):
        for rowIdx in range(rows-1):
            idx1 = rowIdx+row_step1
            idx2 = colIdx+col_step1
            idx3 = rowIdx+row_step2
            idx4 = colIdx+col_step2

            if isInvert:
                idx1, idx2 = idx2, idx1
                idx3, idx4 = idx4, idx3

            if board[idx1][idx2] == '-' and board[idx3][idx4] == '-':
                    continue
            elif board[idx1][idx2] == '-' and board[idx3][idx4] != '-':
                return True
            elif board[idx1][idx2] == board[idx3][idx4] and board[idx1][idx2] != '-':
                return True
    return False

def canMoveTiles(direction):
    global board, rows, cols
    if direction == TOP:
        return areTilesMovable(0,0,1,0,rows,cols)
    
    if direction == BOTTOM:
        return areTilesMovable(1,0,0,0,rows,cols)
        
    if direction == LEFT:
        return  areTilesMovable(0,0,1,0,cols,rows,True)
    
    return areTilesMovable(1,0,0,0,cols,rows,True)

def canMergeAny():
    global board, rows, cols
    return areTilesMovable(0,0,1,0,rows,cols) or \
         areTilesMovable(1,0,0,0,rows,cols) or \
             areTilesMovable(0,0,1,0,cols,rows,True) or \
                 areTilesMovable(1,0,0,0,cols,rows,True)
    
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
        shiftTilesTop(colIdx)
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
        shiftTilesBottom(colIdx)
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
        shiftTilesLeft(rowIdx)
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
        shiftTilesRight(rowIdx)
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
    i = 0
    while i < rows - 1:
        if board[i][colIdx] != '-':
            i+=1
            continue

        j = i+1
        while j<rows and board[j][colIdx] == '-':
            j+=1
        
        if j != rows:
            board[i][colIdx] = board[j][colIdx]
            board[j][colIdx] = '-'
            i = j
            j += 1
        else:
            break
    

def shiftTilesBottom(colIdx):
    global board, rows
    i = rows - 1
    while i > 0:
        if board[i][colIdx] != '-':
            i-=1
            continue

        j = i-1
        while j>=0 and board[j][colIdx] == '-':
            j-=1
        
        if j >= 0:
            board[i][colIdx] = board[j][colIdx]
            board[j][colIdx] = '-'
            i = j
            j -= 1
        else:
            break

def shiftTilesLeft(rowIdx):
    global board, cols
    i = 0
    while i < cols - 1:
        if board[rowIdx][i] != '-':
            i+=1
            continue

        j = i+1
        while j<cols and board[rowIdx][j] == '-':
            j+=1
        
        if j != cols:
            board[rowIdx][i] = board[rowIdx][j]
            board[rowIdx][j] = '-'
            i = j
            j += 1
        else:
            break

def shiftTilesRight(rowIdx):
    global board, cols
    i = cols - 1
    while i > 0:
        if board[rowIdx][i] != '-':
            i-=1
            continue

        j = i-1
        while j>=0 and board[rowIdx][j] == '-':
            j-=1
        
        if j >=0:
            board[rowIdx][i] = board[rowIdx][j]
            board[rowIdx][j] = '-'
            i = j
            j -= 1
        else:
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