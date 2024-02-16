# Kazdy labirynt ma opisane pole startu jako O i koniec jako X, program szuka najkrotszej sciezki miedzy tymi punktami

# Do rozwiazania problemu znalezienia najkrotszej sciezki w labiryncie uzywamy algorytmu przeszukiwania wszerz (BFS). 
# Algorytm ten polega na badaniu stopniowego sasiedztwa wierzcholkow, zaczynajac od wierzcholka startowego. 
# W trakcie badania kazdy wierzcholek jest odwiedzany, a jego sasiedzi dodawani sa do kolejki. 
# Proces ten powtarzany jest do momentu odnalezienia celu (w tym przypadku wyjscia z labiryntu) lub sprawdzenia wszystkich mozliwych sciezek.

# Algorytm BFS jest stosowany w tym kontekscie, poniewaz gwarantuje znalezienie najkrotszej sciezki w nieskierowanym grafie, 
# a labirynt mozna traktowac jako graf, gdzie kazde pole jest wierzcholkiem, a mozliwe ruchy miedzy polami to krawedzie. 
# Algorytm ten ma zastosowanie do problemow przeszukiwania w grafach bez wag krawedzi, co sprawia, ze jest odpowiedni w przypadku labiryntow, 
# gdzie wszystkie kroki maja taka sama wage.

import queue
import time

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

def createLabirynt2():
    labirynt = [
        "##########",
        "O     #  #",
        "####  #  #",
        "#        #",
        "#  ####  #",
        "#  #     X",
        "##########"
    ]
    return [list(row) for row in labirynt]

def createLabirynt3():
    labirynt = [
        "###############################",
        "O        #  #           #     #",
        "#  #  ####  #  #######  #  ####",
        "#  #     #        #           #",
        "#  #######  #  ##########  ####",
        "#           #  #  #  #     #  #",
        "#  ####  ####  #  #  ####  #  #",
        "#  #        #  #  #     #     #",
        "#  #  #######  #  #  #  #  ####",
        "#  #        #        #  #  #  #",
        "#  ####  ####  ##########  #  #",
        "#     #  #              #  #  #",
        "##########  ####  #  ####  #  #",
        "#     #     #     #  #  #  #  #",
        "####  #######  #######  ####  #",
        "#     #  #                 #  #",
        "#  ####  ####  ##########  #  #",
        "#  #              #     #     #",
        "#  #  ####  ####  #  ####  #  #",
        "#     #     #           #  #  X",
        "###############################",
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

def find_shortest_path(labirynt, start, end):
    rows, cols = len(labirynt), len(labirynt[0])
    visited = set()
    shortest_sciezka = None
    shortest_kroki = float('inf')
    q = queue.Queue()
    q.put((start, 0, []))

    while not q.empty():
        (current_row, current_col), kroki, current_sciezka = q.get()

        if (current_row, current_col) == end:
            if kroki < shortest_kroki:
                shortest_kroki = kroki
                shortest_sciezka = current_sciezka
            continue

        if (current_row, current_col) not in visited:
            visited.add((current_row, current_col))

            ruchy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for ruch in ruchy:
                new_row, new_col = current_row + ruch[0], current_col + ruch[1]
                if is_valid_move(labirynt, new_row, new_col):
                    new_sciezka = current_sciezka + [(new_row, new_col)]
                    q.put(((new_row, new_col), kroki + 1, new_sciezka))

    if shortest_sciezka is not None:
        return set(shortest_sciezka), shortest_kroki
    else:
        return None, float('inf')

if __name__ == "__main__":
    labirynt1 = createLabirynt1()
    labirynt2 = createLabirynt2()
    labirynt3 = createLabirynt3()

    # Pomiar czasu dla Labiryntu 1
    start_time = time.time()
    start1, end1 = (1, 0), (5, 5)
    sciezka1, kroki1 = find_shortest_path(labirynt1, start1, end1)
    end_time = time.time()
    elapsed_time1 = end_time - start_time

    print(f"\nLabirynt 1 - Najkrotsza Sciezka (Kroki: {kroki1}), Czas: {elapsed_time1:.6f} sekundy")
    printLabirynt(labirynt1, sciezka1)

    # Pomiar czasu dla Labiryntu 2
    start_time = time.time()
    start2, end2 = (1, 0), (5, 9)
    sciezka2, kroki2 = find_shortest_path(labirynt2, start2, end2)
    end_time = time.time()
    elapsed_time2 = end_time - start_time

    print(f"\nLabirynt 2 - Najkrotsza Sciezka (Kroki: {kroki2}), Czas: {elapsed_time2:.6f} sekundy")
    printLabirynt(labirynt2, sciezka2)

    # Pomiar czasu dla Labiryntu 3
    start_time = time.time()
    start3, end3 = (1, 0), (19, 29)
    sciezka3, kroki3 = find_shortest_path(labirynt3, start3, end3)
    end_time = time.time()
    elapsed_time3 = end_time - start_time

    print(f"\nLabirynt 3 - Najkrotsza Sciezka (Kroki: {kroki3}), Czas: {elapsed_time3:.6f} sekundy")
    printLabirynt(labirynt3, sciezka3)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(36, activation='softmax')
])