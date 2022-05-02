"""CS 108 PROJECT

This is a test with many asserts to test  that the code is implementing the components the right way

@author: Hadong Park (hp55)
@date: Spring, 2022
"""

import unittest 
from worlds_best_tic_tac_toe import Canvas, __init__, App

class CanvasTestCase(unittest.TestCase):
    def canvas_unit(self, app):
        result = __init__(UNIT)
        self.assertEqual(result,  700)
    
    def canvas_control_unit(self, app):
        height_result = __init(CONTROL_UNIT)
        self.assertEqual(height_result, 500)
        
class ScoreTestCase(unittest.TestCase):
    def score_x(self, app):
        score_x_result = score_X
        self.assertEqual(score_x_result, 0)
    
    def score_O(self, app):
        score_o_result = score_O
        self.assertEqual(score_o_result, 1)
    


print("all test passed")



