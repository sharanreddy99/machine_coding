import unittest
import snakeandladder
from unittest.mock import patch

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        # Board Size
        '10 10',

        # No of Snakes
        '5',
        # N Snakes
        '15 5','26 18','45 42','74 61','92 60',

        # No of Ladders
        '1',
        # N Ladders
        '43 73',
        
        # No of Players
        '2',
        # N Players
        'Sharan',
        'Shoeb'
        ])
    def test_using_side_effect(self, mock_input):
        # res = snakeandladder.createBoard()
        pass

    @patch('builtins.input', side_effect=[
        # Board Size
        '10 15',

        # No of Snakes
        '5',

        # No of Ladders
        '1',

        # No of Players
        '3',
        # N Players
        'Sharan',
        'Shoeb',
        'Phalguna'
        ])
    def test_auto_snake_ladder_board(self, mock_input):
        res = snakeandladder.createBoard(True)