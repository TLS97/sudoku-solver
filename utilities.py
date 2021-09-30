import cell

knight = False
king = False


def empty_cell(b):
    for i in range(9):
        for j in range(9):
            if b[i][j].num == 0:
                return i, j
    return False


def print_board(b):
    print("\nBoard: ")
    for i in range(9):
        if (i == 3) or (i == 6):
            print("- - - - - - - - - - -")
        print("{} {} {} | {} {} {} | {} {} {}".format(b[i][0].num, b[i][1].num, b[i][2].num, b[i][3].num, b[i][4].num,
                                                      b[i][5].num, b[i][6].num, b[i][7].num, b[i][8].num))


def apply_constraints(cons):
    global knight, king

    if cons == "kn":
        knight = True
        print("Knight is True")
    elif cons == "ki":
        king = True
    elif cons == "r":
        knight = False
        king = False
    else:
        print("Error: Constraint not valid!")

    return knight, king


def check_row_col_box(b, n, row, col):
    for i in range(9):
        if b[i][col].num == n:
            return False
    for i in range(9):
        if b[row][i].num == n:
            return False
    r = (row // 3) * 3
    c = (col // 3) * 3
    for di in range(0, 3):
        for dj in range(0, 3):
            if b[di + r][dj + c].num == n:
                return False
    return True


def check_knight(b, n, row, col):
    for i in range(row - 2, row + 3, 4):
        for j in range(col - 1, col + 2, 2):
            if (row, col) != (i, j) and (0 < i < 9) and (0 < j < 9):
                if b[i][j].num == n:
                    print("Knight not valid")
                    return False

    for i in range(row - 1, row + 2, 2):
        for j in range(col - 2, col + 3, 4):
            if (row, col) != (i, j) and (0 < i < 9) and (0 < j < 9):
                if b[i][j].num == n:
                    print("Knight not valid")
                    return False
    return True


def check_king(b, n, row, col):
    for dr in range(row - 1, row + 2):
        for dc in range(col - 1, col + 2):
            if row != dr and col != dc and 0 <= dr < 9 and 0 <= dc < 9:
                if b[dr][dc].num == n:
                    return False
    return True


def validity(b, n, row, col):
    if knight == True:
        return check_row_col_box(b, n, row, col) and check_knight(b, n, row, col)
    elif king == True:
        return check_row_col_box(b, n, row, col) and check_king(b, n, row, col)
    else:
        return check_row_col_box(b, n, row, col)

# def check_correctness(b):
#     checklist = []
#     for i in range(9):
#         for j in range(9):
#             if check_validity(b, b[i][j].num, i, j):
#                 checklist.append(True)
#     if all(checklist):
#         return True
#
#
# def decision(b):
#     # If board is full
#     if not empty_cell(b) and check_correctness(b):
#         print("The solution is correct")
#     else:
#         for i in range(9):
#             for j in range(9):
#                 if b[i][j].num != 0:
#                     if validity(b, b[i][j].num, i, j):
#                         print("Board number: {}, Row: {}, Col: {}".format(b[i][j].num, i, j))
#                         return True
#                     else:
#                         return False