import unittest
from src.sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.grid = [
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
        self.doku = Sudoku(self.grid)

    def test_find_none(self):
        self.assertEqual((0, 0), self.doku.find_next_none())

    def test_find_none_v2(self):
        grid = [
            [5, 9, 6, 2, 6, 7, 7, 8, 1],
            [6, 8, 6, None, 7, None, None, 9, None],
            [1 ,9, None, None, None, 4, 5, None, None],
            [8, 2, None, 1, None, None, None, 4, None],
            [None, None, 4, 6, None, 2, 9, None, None],
            [None, 5, None, None, None, 3, None, 2, 8],
            [None, None, 9, 3, None, None, None, 7, 4],
            [None, 4, None, None, 5, None, None, 3, 6],
            [7, None, 3, None, 1, 8, None, None, None]
        ]
        self.doku_2 = Sudoku(grid)
        self.assertEqual((1, 3), self.doku_2.find_next_none())

    def test_check_in_row_true(self):
        self.assertEqual(True, self.doku.check_in_row(2, 0))

    def test_check_in_row_false(self):
        self.assertEqual(False, self.doku.check_in_row(3, 0))

    def test_check_in_column_true(self):
        self.assertEqual(True, self.doku.check_in_column(1, 0))

    def test_check_in_column_false(self):
        self.assertEqual(False, self.doku.check_in_column(4, 0))

    def test_check_in_square_true(self):
        self.assertEqual(True, self.doku.check_in_square(6, 0, 0))

    def test_check_in_square_false(self):
        self.assertEqual(False, self.doku.check_in_square(8, 6, 6))

    #no tests for construct_inner_matrix