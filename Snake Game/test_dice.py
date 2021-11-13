import unittest
from dice import Dice
from unittest.mock import patch

class Test(unittest.TestCase):

    def test_can_throw_again(self):
        test_cases = [
            {
            "no_of_dice": 1,
            "six_limit": 3,
            "current_throw": [6],
            "expected_resp": True
            },
            {
            "no_of_dice": 1,
            "six_limit": 3,
            "current_throw": [4],
            "expected_resp": False
            },
            {
            "no_of_dice": 2,
            "six_limit": 3,
            "current_throw": [4, 6],
            "expected_resp": True
            },
            {
            "no_of_dice": 2,
            "six_limit": 3,
            "current_throw": [2, 3],
            "expected_resp": False
            }
        ]
        
        for test_case in test_cases:
            # Setup
            dice = Dice(test_case["no_of_dice"],test_case["six_limit"])
            
            # Execute
            res = dice.can_throw_again(test_case["current_throw"])
            
            # Validate
            self.assertEqual(res,test_case["expected_resp"])

    def test_roll_dice(self):
        test_cases = [
            {
            "no_of_dice": 1,
            "six_limit": 3
            },
            {
            "no_of_dice": 1,
            "six_limit": 3
            },
            {
            "no_of_dice": 2,
            "six_limit": 3
            },
            {
            "no_of_dice": 2,
            "six_limit": 3
            }
        ]
        
        for test_case in test_cases:
            # Setup
            dice = Dice(test_case["no_of_dice"],test_case["six_limit"])
            
            # Execute
            res = dice.roll_dice()
            
            # Validate
            for val in res:
                self.assertLessEqual(val,test_case["no_of_dice"]*6)