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

    def check_valid(self, number, row_index, column_index):
        row_invalid = self.check_in_row(number, row_index)
        column_invalid = self.check_in_column(number, column_index)
        square_invalid = self.check_in_square(number, row_index, column_index)
        if not row_invalid and not column_invalid and not square_invalid:
            return True
        return False

    def check_in_row(self, number, row_index):
        for cell in self.matrix[row_index]:
            if cell == number:
                return True
        return False

    def check_in_column(self, number, column_index):
        for row in self.matrix:
            if row[column_index] == number:
                return True
        return False

    def construct_inner_matrix(self, row_index, column_index):
        inner_matrix_pos = (int(row_index / 3) , int(column_index / 3))
        inner_matrix_rows = self.matrix[ inner_matrix_pos[0] * 3 : (inner_matrix_pos[0] + 1) * 3 ]
        inner_matrix_final = []
        for row in inner_matrix_rows:
            stripped_row = row[ inner_matrix_pos[1] * 3 : (inner_matrix_pos[1] + 1) * 3]
            inner_matrix_final.append(stripped_row)
        return inner_matrix_final

    def check_in_square(self, number, row_index, column_index):
        inner_matrix = self.construct_inner_matrix(row_index, column_index)
        for row in inner_matrix:
            if number in row:
                return True
        return False



