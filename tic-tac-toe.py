# variables
rows = 0
cols = 0
no_of_players = 0
playerName = {None: 'Initial Board'}
pieceShapes = {}
board = []

def startGame(isCustomBoard = False):
    try:
        if isCustomBoard:
            setCustomBoard()
        else:
            initializeBoard()
        fileWrite('result.txt','w','Board Moves\n-----------\n')   
        printBoard(None)
        current_player = 0
        while emptySlotExists():
            rowIdx, colIdx = getMove(current_player)
            if isValidMove(rowIdx,colIdx):
                makeMove(rowIdx,colIdx,pieceShapes[current_player])
                printBoard(current_player)
                if checkGameWon(current_player):
                    print('Congratulations '+playerName[current_player]+' for winnning the game')
                    restartGame()
                current_player = (current_player+1)%no_of_players
            else:
                print('\n invalid move. Please choose a valid one')
        else:
            restartGame()
    except Exception as e:
        print(e)

def initializeBoard():
    global rows, cols, board, no_of_players
    rows = int(input("\nEnter grid size: "))
    cols = rows 
    no_of_players = int(input("\nEnter no of players: "))
    for i in range(no_of_players):
        name,shape = input('\nChoose the name and shape for Player - '+str(i+1)+': ').split() 
        pieceShapes[i] = shape
        playerName[i] = name

    board = [['-' for i in range(cols)] for j in range(rows)]

def printBoard(position):

    print('\n Board:\n ------\n')
    print('Player: '+playerName[position]+'\n')
    global board
    for row in board:
        for tile in row:
            print(tile,end=' ')
        print()
    print()

    global fp
    rowStr = 'Player: '+playerName[position]+'\n'
    for row in board:
        for tile in row:
            rowStr += str(tile) + ' ' 
        rowStr += '\n'
    rowStr += '\n\n----------------------\n\n'

    fileWrite('result.txt','a',rowStr)

def fileWrite(fileName,mode,value):
    fp = open(fileName,mode)
    fp.write(value)
    fp.close()

def emptySlotExists():
    global board
    for row in board:
        for slot in row:
            if slot == '-':
                return True
    return False

def getMove(current_player):
    rowIdx, colIdx = map(int,input("\n Player "+str(current_player+1)+': Please enter you position to mark: ').split())
    return rowIdx-1, colIdx-1

def restartGame():
    isRestart = int(input('\nGameOver. Press 1 to restart'))
    if isRestart == 1:
        startGame()
    else:
        print('Thankyou for playing the game.')

def isValidMove(rowIdx,colIdx):
    return board[rowIdx][colIdx] == '-'

def makeMove(rowIdx,colIdx,shape):
    board[rowIdx][colIdx] = shape

def checkGameWon(current_player):
    global rows,cols
    for i in range(cols):
        if checkRow(0,i,rows,i+1,1,1,current_player):
            return True
    
    for i in range(rows):
        if checkRow(i,0,i+1,cols,1,1,current_player):
            return True
    
    if checkRow(0,0,rows,cols,1,1,current_player) or checkRow(0,cols-1,rows,-1,1,-1,current_player):
        return True
    return False

def checkRow(row_start,col_start,row_end,col_end,row_step,col_step,current_player):
    global board, pieceShapes

    piece = pieceShapes[current_player]
    for rowIdx in range(row_start,row_end,row_step):
        for colIdx in range(col_start,col_end,col_step):
            if board[rowIdx][colIdx] != piece:
                return False
    return True

def setCustomBoard():
    global board,rows,cols
    rows = 2
    cols = 2
    board = [['-' for i in range(cols)] for j in range(rows)]
    playerName = {0: 'Sharan', 1: 'Shoeb'}
    pieceShapes = {0: 'X', 1: 'O'}
    arr = [(0,0,pieceShapes[0]),(0,1,pieceShapes[0]),(1,0,pieceShapes[1]),(1,1,pieceShapes[1])]
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

if __name__ == '__main__':
    startGame()