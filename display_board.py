class DisplayBoard:
    @staticmethod
    def display(board: list) -> str:
        board_string = ""
        for row in board:
            for column in row:
                board_string += f"{column} "
            board_string += "\n"
        return board_string
