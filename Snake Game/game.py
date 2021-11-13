import constants
from input import Input
from dice import Dice
from validation import Validation

class Game:
    validation = None
    grid_length = 0
    players = []
    positions = []
    available_snake_slots = {}
    available_ladder_slots = {}
    snakes = {}
    ladders = {}
    no_of_dice = 0
    six_limit = 0

    def __init__(self, no_of_dice=1, six_limit=3):
        self.validation = Validation(self)
        self.no_of_dice = no_of_dice,
        self.six_limit = six_limit
        
    def start_game(self):
        try:
            is_auto_create = input(constants.AUTO_CREATE_MESSAGE)

            Input(self,is_auto_create.lower() == 'y')
            self.run()
        except Exception as e:
            print(constants.EXCEPTION_MESSAGE.format(str(e)))

    def run(self):
        current_player = 0
        dice = Dice(self.no_of_dice, self.six_limit)

        while True:
            if len(self.players) == 1:
                print(constants.PLAYER_LOST_STMT.format(self.players[0]))
                return

            current_throw = dice.roll_dice()
            if not self.validation.can_move(current_throw, current_player):
                current_player = (current_player + 1)%len(self.players)
                continue

            for val in current_throw:
                newposition = self.move_player(current_player, val)
                self.positions[current_player] = newposition
                if self.check_won(current_player, newposition):
                    current_player -= 1
            
            current_player = (current_player + 1)%len(self.players)

    def store_position(self, name, head, tail):
        if name == constants.SNAKE:
            self.snakes[head] = tail
        else:
            self.ladders[head] = tail

        del self.available_snake_slots[head]
        del self.available_ladder_slots[head]
    
    def check_won(self, current_player, position):
        if position == self.grid_length:
            print(constants.PLAYER_WON_STMT.format(self.players[current_player]))
            self.players.pop(current_player)
            self.positions.pop(current_player)
            return True
        return False
    
    def move_player(self, current_player, throw):
        position = self.positions[current_player]
        if position + throw > self.grid_length:
            return position
        
        oldpos = position
        position += throw
        while True:
            if self.snakes.get(position) != None:
                position = self.snakes[position]
            elif self.ladders.get(position) != None:
                position = self.ladders[position]
            else:
                break
        
        print(constants.DICE_ROLL_STMT.format(self.players[current_player],throw,oldpos,position))
        return position
