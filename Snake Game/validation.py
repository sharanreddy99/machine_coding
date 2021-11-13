import constants
from game import Game

class Validation:
    game: Game = None
    def __init__(self, game: Game):
        self.game = game

    def is_valid_position(self, name, head, tail):
        if head <= tail:
            return False
    
        if not self.game.available_snake_slots[head] or not self.game.available_ladder_slots[head]:
            return False
        
        if name == constants.SNAKE and self.game.ladders.get(tail) != None and self.game.ladders[tail] == head:
            return False
        
        if name == constants.LADDER and self.game.snakes.get(tail) != None and self.game.snakes[tail] == head:
            return False

        return True

    def can_move(self, current_throw, current_player):
        position = self.game.positions[current_player]
        for val in current_throw:
            if position+ val > self.game.grid_length:
                return False
            
            position += val
            while True:
                if self.game.snakes.get(position) != None:
                    position = self.game.snakes[position]
                elif self.game.ladders.get(position) != None:
                    position = self.game.ladders[position]
                else:
                    break
        return True