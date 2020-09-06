from copy import deepcopy

def find_number(table, row, col, val):
    for i in range(9):
        if table[i][col] == val or table[row][i] == val:
            return 0
    for i in range(3):
        for j in range(3):
            if table[row - (row % 3) + i][col - (col % 3) + j] == val:
                return 0
    return 1


def solve(table, value):
    x = value // 9
    y = value % 9
    if value == 81:
        return 1
    if table[x][y] != 0:
        return solve(table, value + 1)
    for i in range(1, 10):

        if find_number(table, x, y, i):
            table[x][y] = i
            if solve(table, value + 1):
                return 1
            else:
                table[x][y] = 0
    return 0


def rev_solve(table, value):
    i = 9
    x = value // 9
    y = value % 9
    if value == 81:
        return table
    if table[x][y] != 0:
        return solve(table, value + 1)
    for i in range(1, 10):
        if find_number(table, x, y, i):
            table[x][y] = i
            if rev_solve(table, value + 1):
                return 1
            else:
                table[x][y] = 0
    return 0


def check(table):
    rev_table = deepcopy(table)
    if solve(table, 0) != 0 and rev_solve(rev_table, 0) != 0:
        if table == rev_table:
            return 1
    return 0

