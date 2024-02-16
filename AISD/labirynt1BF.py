import itertools

def createLabirynt1():
    labirynt = [
        "#######",
        "O     #",
        "##### #",
        "#     #",
        "#  ####",
        "#     X",
        "#######"
    ]
    return [list(row) for row in labirynt]

def printLabirynt(labirynt, sciezka=None):
    if sciezka is None:
        sciezka = set()

    for i, row in enumerate(labirynt):
        for j, cell in enumerate(row):
            if (i, j) in sciezka:
                print("+", end="")
            else:
                print(cell, end="")
        print()

def is_valid_move(labirynt, row, col):
    rows, cols = len(labirynt), len(labirynt[0])
    return 0 <= row < rows and 0 <= col < cols and labirynt[row][col] != "#"

def brute_force_shortest_path(labirynt, start, end):
    rows, cols = len(labirynt), len(labirynt[0])
    all_paths = list(itertools.product([-1, 0, 1], repeat=rows*cols-2))
    shortest_path = None
    shortest_steps = float('inf')

    for path in all_paths:
        current_row, current_col = start
        steps = 0
        current_path = [(current_row, current_col)]

        for move in path:
            new_row, new_col = current_row + move // cols, current_col + move % cols
            if is_valid_move(labirynt, new_row, new_col):
                current_row, current_col = new_row, new_col
                current_path.append((current_row, current_col))
                steps += 1

                if (current_row, current_col) == end:
                    if steps < shortest_steps:
                        shortest_steps = steps
                        shortest_path = current_path

    return set(shortest_path), shortest_steps

if __name__ == "__main__":
    labirynt1 = createLabirynt1()

    start1, end1 = (1, 0), (5, 5)

    sciezka1_bf, kroki1_bf = brute_force_shortest_path(labirynt1, start1, end1)

    print(f"\nLabirynt 1 - Brute Force: Kroki: {kroki1_bf}")
    printLabirynt(labirynt1, sciezka1_bf)
