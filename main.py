from algoritm import check


def print_sudoku(table, msg):
    print(msg)
    for i in range(9):
        for j in range(9):
            if j != 8:
                print(f"{table[i][j]}|", end='')
            else:
                print(table[i][j])
        if i != 8:
            if (i + 1) % 3 == 0:
                print(str('-----|' * 2) + str("-" * 5))
            else:
                print(str('- - -|' * 2) + str("- " * 3))


print("Import sudoku table:\n")
table = []
for i in range(9):
    table.append(input())
sudoku_table = []
for line in table:
    new_line = []
    if len(line) != 9:
        exit("Error")
    for elem in line:
        if elem == '.':
            new_line.append(0)
        elif elem in "0123456789":
            new_line.append(int(elem))
        else:
            exit("Error")
    sudoku_table.append(new_line)
print_sudoku(sudoku_table, "Imported sudoku:\n")
if check(sudoku_table):
    print_sudoku(sudoku_table, "\nSolved sudoku:\n")

else:
    print("Bad sudoku!")