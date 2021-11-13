import constants
from validation import Validation
from random import choice

class Input:
    auto_create = False
    game = None
    validation = None
    
    def __init__(self, game, auto_create):
        self.game = game
        self.validation = Validation(game)
        self.auto_create = auto_create
        self.read()

    def read(self):
        try:
            self.read_grid_length()
            self.read_objects()
            self.read_players()
            
        except Exception as e:
            print(constants.EXCEPTION_MESSAGE.format(str(e)))

    def read_grid_length(self):
        rows,cols = map(int, input(constants.READ_ROWS_COLS_STMT).split())
        self.game.grid_length = rows*cols
            
    def read_objects(self):
        self.game.available_snake_slots = {slot: True for slot in range(1, self.game.grid_length)}
        self.game.available_ladder_slots = {slot: True for slot in range(1, self.game.grid_length)}

        no_of_snakes = self.read_additional_items(constants.SNAKE, self.game.grid_length-2)
        no_of_ladders = self.read_additional_items(constants.LADDER, self.game.grid_length-2-no_of_snakes)

        if self.auto_create:
            self.auto_create_board(no_of_snakes, no_of_ladders)

    def read_players(self):
        no_of_players = int(input(constants.READ_PLAYERS_COUNT))
        for i in range(no_of_players):
            name = input(constants.READ_PLAYER_DETAILS.format(i+1))
            self.game.players.append(name)
            self.game.positions.append(0)

    def read_additional_items(self, name, limit):
        no_of_objects= 0
        while True:
            no_of_objects = int(input(constants.READ_OBJECT_WITH_NAME.format(name)))
            if no_of_objects > limit:
                print(constants.READ_OBJECT_LIMIT_EXCEEDED.format(name))
                continue

            if not self.auto_create:
                n = no_of_objects
                while n>0:
                    head, tail = map(int,input(constants.READ_OBJECT_POSITION.format(name)).split())
                    if name == constants.SNAKE:
                        
                        if not self.validation.is_valid_position(constants.SNAKE, head, tail):
                            print(constants.OBJECT_INVALID_POSITION.format(constants.SNAKE))
                            continue
                        
                        self.game.store_position(constants.SNAKE, head, tail)
                        n -= 1
                    elif name == constants.LADDER:
                        if not self.validation.is_valid_position(constants.LADDER, tail, head):
                            print(constants.OBJECT_INVALID_POSITION.format(constants.LADDER))
                            continue
                        
                        self.game.store_position(constants.LADDER, head, tail)
                        n -= 1
            return no_of_objects

    def auto_create_board(self, no_of_snakes, no_of_ladders):
        while no_of_snakes > 0:
            snake_head_slots = list(self.game.available_snake_slots.keys())
            head_choice = choice(snake_head_slots)
            snake_tail_shots = list(filter(lambda x: x<head_choice, snake_head_slots))
            if len(snake_tail_shots) == 0:
                del self.game.available_snake_slots[head_choice]
                continue
            
            tail_choice = choice(snake_tail_shots)
            self.game.store_position(constants.SNAKE, head_choice, tail_choice)
            no_of_snakes -= 1
        
        while no_of_ladders > 0:
            ladder_head_slots = list(self.game.available_ladder_slots.keys())
            head_choice = choice(ladder_head_slots)
            ladder_tail_slots = list(filter(lambda x: x>head_choice,snake_head_slots))
            if len(ladder_tail_slots) == 0:
                del self.game.available_ladder_slots[head_choice]
                continue
            
            while len(ladder_tail_slots) > 0:
                tail_choice = choice(ladder_tail_slots)
                if self.game.snakes.get(tail_choice) == None:
                    self.game.store_position(constants.LADDER, head_choice, tail_choice)
                    no_of_ladders -= 1
                    break

                position = self.game.snakes[tail_choice]
                while True:
                    if self.game.snakes.get(position) != None:
                        position = self.game.snakes[position]
                    elif self.game.ladders.get(position) != None:
                        position = self.game.snakes[position]
                    else:
                        break

                    if position == head_choice:
                        position = -1
                
                if position == -1:
                    ladder_tail_slots.remove(tail_choice)
                else:
                    self.game.store_position(constants.LADDER, head_choice, tail_choice)
                    no_of_ladders -=1
                    break
        
            else:
                del self.game.available_ladder_slots[head_choice]    