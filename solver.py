import cell
import utilities


# Recursive algorithm
def solve(b):
    # Base condition
    if not utilities.empty_cell(b):
        return True
    else:
        row, col = utilities.empty_cell(b)
        for i in range(1, 10):
            if utilities.validity(b, i, row, col):
                b[row][col].num = i
                if solve(b):
                    return True
                b[row][col].num = 0
    return False


# An empty board is created (9x9)
board = [[cell.Cell(n=0) for i in range(9)] for j in range(9)]

list_of_strings = []
print("Enter numbers in the board row by row (0 for empty cells, e.g. 120456009)")
for i in range(9):
    r = [input("--> ")]
    list_of_strings.append(r)

# Converts 1D-list of strings to 1D-list of integers
list_of_integers = [int(list_of_strings[i][0][j]) for i in range(9) for j in range(9)]

# Converts 1D-list to 2D-list (from StackOverflow)
list2d = [list_of_integers[i:i+9] for i in range(0, 80, 9)]

# Insert the number inputted by user in the cells
for i in range(9):
    for j in range(9):
        board[i][j].num = list2d[i][j]

# The user inputs if they want Anti-Knight or Anti-King constraints applied
print("\nConstraints:\nAnti-Knight -> kn\nAnti-King -> ki\nRegular -> r")
constraints = input("\nEnter desired constraints: ")
kn, ki = utilities.apply_constraints(constraints)

solve(board)
utilities.print_board(board)

# If the board is already full - check constraints - return if its correct or not
# If the board is not full - check that none of the numbers added by user is invalid - if not, solve the board
# if utilities.decision(board):
#     solve(board)
#     utilities.print_board(board)
# else:
#     print("Sudoku Board is not solvable!")



