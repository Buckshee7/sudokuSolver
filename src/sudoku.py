class Sudoku:
    def __init__(self, grid):
        self.matrix = grid

    def solve(self):
        pass
    
    def find_next_none(self):
        for row in range(len(self.matrix)):
            for cell in range(len(self.matrix[row])):
                if self.matrix[row][cell] == None:
                    return (row, cell)

    def check_valid(self, number, row, column):
        row_valid = self.check_in_row(number, row)
        column_valid = self.check_in_column(number)
        square_valid = self.check_in_square(number)

    def check_in_row(self, number, row):
        pass

    def check_in_column(self, number, column):
        pass

    def check_in_square(self, number, row, column):
        pass
