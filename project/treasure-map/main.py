import string


def create_map(cols, rows):
    return [["⬜️" for _ in range(cols)] for _ in range(rows)]


def x_mark(map, col, row):
    if 0 <= row < len(map) and 0 <= col < len(map[0]):
        map[row][col] = "❌"
    else:
        print("Invalid Input.")


def print_map(map):
    for row in map:
        print(" ".join(row))


def print_grid_with_label(label, map):
    print("  ", "  ".join(label))
    for i, row in enumerate(map, start=1):
        print(i, " ".join(row))


print("Create a Map for Treasure!")

col = int(input("Input Columns in Number (1-26): "))
row = int(input("Input Rows in Number (1-9): "))

map = create_map(col, row)

label = [chr(i) for i in range(ord("A"), ord("A") + col)]
alphabet = list(string.ascii_uppercase)
print_grid_with_label(label, map)

set_mark = input("Set your Treasure Mark (D9): ")
letter = set_mark[0].upper()
col_x = alphabet.index(letter)
row_x = int(set_mark[1]) - 1

x_mark(map, col_x, row_x)

print_grid_with_label(label, map)
