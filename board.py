from display_board import DisplayBoard
from tools import Tools


class Board(DisplayBoard):
    def __init__(self):
        self.board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 7, 2, 6, 0, 4, 8, 0],
            [4, 0, 0, 9, 3, 5, 0, 0, 6],
            [0, 3, 0, 4, 8, 0, 2, 0, 0],
            [0, 4, 1, 6, 0, 9, 3, 0, 0],
            [0, 0, 6, 0, 0, 0, 8, 9, 0],
            [5, 7, 8, 0, 4, 0, 0, 0, 2],
            [0, 0, 0, 3, 0, 0, 0, 7, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 5],
        ]

    def print_board(self):
        print(self.display(self.board))

    def row_exists(self, row: int) -> bool:
        return 1 <= row <= len(self.board)

    def column_exists(self, column: int) -> bool:
        return 1 <= column <= len(self.board[0])

    def row_check(self, row: int, value: int) -> bool:
        selected_row = self.board[row]
        return Tools.in_array(value, selected_row)

    def get_column(self, column: int):
        for i, row in enumerate(self.board):
            print(self.board[i][column-1])

# b = Board()
# b.get_column(2)
