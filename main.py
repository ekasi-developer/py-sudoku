from board import Board


board = Board()

while True:
    board.print_board()
    row = int(input("Please select row: "))
    if board.row_exists(row) is False:
        print("Row does not exist.")
        continue
    column = int(input("Please select columns: "))
    if board.column_exists(column) is False:
        print("Column does not exist.")
        continue
    value = int(input("Enter value: "))
    print(f"Row exists:", board.row_check(row, value))


