import random

def createBoard(autoCreate = False):
    readInput(autoCreate)
    
def readInput(autoCreate):
    global rows,cols,availableSnakeSlots,availableLadderSlots, lastValue

    rows,cols = map(int,input("\nEnter board size(Eg: 10 10): ").split())
    lastValue = rows*cols
    availableSnakeSlots = {i:True for i in range(1,lastValue)}
    availableLadderSlots = {i:True for i in range(1,lastValue)}
    
    no_of_snakes = readAdditionalItems(SNAKE,autoCreate,lastValue-2)
    no_of_ladders = readAdditionalItems(LADDER,autoCreate,lastValue-2-no_of_snakes)

    if autoCreate:
        autoCreateSnakesAndLadders(no_of_snakes,no_of_ladders)
    
    readPlayers()
    startGame()

def startGame():
    global positions
    currentPlayer = 0
    while True:
        if len(players) == 1:
            print('{0} lost the game.'.format(players[0]))
            return

        diceVal = rollDice()

        if not canMove(diceVal,positions[currentPlayer]):
            currentPlayer = (currentPlayer + 1)%len(players)
            continue

        for val in diceVal:
            newposition = movePlayer(currentPlayer, val)
            positions[currentPlayer] = newposition
            if checkWon(currentPlayer, newposition):
                currentPlayer -= 1
        
        currentPlayer = (currentPlayer + 1)%len(players)

def canMove(diceval,pos):
    if pos+sum(diceval) > lastValue:
        return False
    return True

def movePlayer(currentPlayer,val):
    position = positions[currentPlayer]
    if position+val > lastValue:
        return position
    
    oldpos = position
    position += val
    while True:
        if snakes.get(position) != None:
            position = snakes[position]
        elif ladders.get(position) != None:
            position = ladders[position]
        else:
            break
    
    print('{0} rolled a {1} and moved from {2} to {3}'.format(players[currentPlayer],val,oldpos,position))
    return position


def checkWon(currentPlayer,pos):
    global players,positions
    if pos == lastValue:
        print('{0} wins the game'.format(players[currentPlayer]))
        players.pop(currentPlayer)
        positions.pop(currentPlayer)
        return True
    return False
            
def rollDice():
    diceval = []
    for _ in range(3):
        val = random.randrange(1,7)
        diceval.append(val)
        if val != 6:
            break
    
    diceval = clearMove(diceval)
    return diceval

def clearMove(diceval):
    for val in diceval:
        if val != 6:
            return diceval
    else:
        return []

def readPlayers():
    no_of_players = int(input('\nEnter no of players: '))
    for i in range(no_of_players):
        name = input("Enter name of Player {0}: ".format(i+1))
        players.append(name)
        positions.append(0)
        
def readAdditionalItems(name,autoCreate,limit):
    no_of_objects= 0
    while True:
        no_of_objects = int(input('\nEnter no of {0}: '.format(name)))
        if no_of_objects > limit:
            print('\nThe limit for no of {0} in the board has exceeded. Please try again'.format(name))
            continue
        if not autoCreate:
            n = no_of_objects
            while n>0:
                head, tail = map(int,input('\nEnter head and tail of {0}: '.format(name)).split())
                if name == SNAKE:
                    
                    if not checkValidPosition(snakes,ladders,head,tail):
                        print('\nPosition is already occupied or cannot be chosen')
                        continue
                    
                    storePosition(SNAKE,head,tail)
                    n -= 1
                else:
                    if not checkValidPosition(ladders,snakes,tail,head):
                        print('\nPosition is already occupied or cannot be chosen')
                        continue
                    
                    storePosition(LADDER,head,tail)
                    n -= 1
        return no_of_objects

def checkValidPosition(obj1,obj2,head,tail):
    if head <= tail:
        return False
    
    if not availableSnakeSlots[head] or not availableLadderSlots[head]:
        return False
    
    if obj2.get(tail) != None and obj2[tail] == head:
        return False
    
    return True
    
def storePosition(name,head,tail):
    global availableSnakeSlots, availableLadderSlots, snakes, ladders
    if name == SNAKE:
        snakes[head] = tail
    else:
        ladders[head] = tail

    del availableSnakeSlots[head]
    del availableLadderSlots[head]

def autoCreateSnakesAndLadders(no_of_snakes,no_of_ladders):
    global snakes,ladders,availableLadderSlots,availableSnakeSlots
    while no_of_snakes > 0:
        snakeHeadSlots = list(availableSnakeSlots.keys())
        headChoice = random.choice(snakeHeadSlots)
        snakeTailSlots = list(filter(lambda x: x<headChoice,snakeHeadSlots))
        if len(snakeTailSlots) == 0:
            del availableSnakeSlots[headChoice]
            continue
        
        tailChoice = random.choice(snakeTailSlots)
        storePosition(SNAKE,headChoice,tailChoice)
        no_of_snakes -= 1
    
    while no_of_ladders > 0:
        ladderHeadSlots = list(availableLadderSlots.keys())
        headChoice = random.choice(ladderHeadSlots)
        ladderTailSlots = list(filter(lambda x: x>headChoice,snakeHeadSlots))
        if len(ladderTailSlots) == 0:
            del availableLadderSlots[headChoice]
            continue
        
        while len(ladderTailSlots) > 0:
            tailChoice = random.choice(ladderTailSlots)
            if snakes.get(tailChoice) == None:
                storePosition(LADDER,headChoice,tailChoice)
                no_of_ladders -= 1
                break

            position = snakes[tailChoice]
            while True:
                if snakes.get(position) != None:
                    position = snakes[position]
                elif ladders.get(position) != None:
                    position = ladders[position]
                else:
                    break

                if position == headChoice:
                    position = -1
            
            if position == -1:
                ladderTailSlots.remove(tailChoice)
            else:
                storePosition(LADDER,headChoice,tailChoice)
                no_of_ladders -=1
                break
    
        else:
            del availableLadderSlots[headChoice]    

    
rows = 0
cols = 0
snakes = {}
ladders = {}
availableSnakeSlots = {}
availableLadderSlots = {}
lastValue = 0
SNAKE = 'snake'
LADDER = 'ladder'
players = []
positions = []