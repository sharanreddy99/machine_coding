from random import choices

class Dice:
    n = 0
    six_limit = 0
    valid_moves = list(range(1,7))
    
    def __init__(self, n=1, six_limit=3):
        self.n = 1
        self.six_limit = 3

    def roll_dice(self):
        rolled_values = []
        for _ in range(3):
            current_throw = choices(self.valid_moves, k=self.n)
            rolled_values.append(sum(current_throw))
            if not self.can_throw_again(current_throw):
                break
        else:
            return []
        return rolled_values
        

    def can_throw_again(self, current_throw):
        for val in current_throw:
            if val == 6:
                return True
        return False
