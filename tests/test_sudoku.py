import unittest
from src.sudoku import Sudoku
from src.cell import Cell

class TestSudoku(unittest.TestCase):
    def setUp(self):
        grid = [
            [None, None, None, 2, 6, None, 7, None, 1],
            [6, 8, None, None, 7, None, None, 9, None],
            [1 ,9, None, None, None, 4, 5, None, None],
            [8, 2, None, 1, None, None, None, 4, None],
            [None, None, 4, 6, None, 2, 9, None, None],
            [None, 5, None, None, None, 3, None, 2, 8],
            [None, None, 9, 3, None, None, None, 7, 4],
            [None, 4, None, None, 5, None, None, 3, 6],
            [7, None, 3, None, 1, 8, None, None, None]
        ]