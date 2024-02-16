import random
import time

def bubble_sort(arr):
    n = len(arr)
    operations = 0
    for i in range(n):
        for j in range(0, n-i-1):
            operations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return operations

def insertion_sort(arr):
    operations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        operations += 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            operations += 1
        arr[j + 1] = key
    return operations

def selection_sort(arr):
    operations = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            operations += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return operations

def comb_sort(arr):
    operations = 0
    gap = len(arr)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(arr):
            operations += 1
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return operations

def shell_sort(arr):
    operations = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            operations += 1
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                operations += 1
            arr[j] = temp
        gap //= 2
    return operations

# Testowanie dla różnych rozmiarów zbiorów
for size in [100, 1000, 10000]:
    arr = [random.randint(1, 10000) for _ in range(size)]

    # Pomiar czasu i ilości operacji dla każdej metody sortowania
    results = []

    start_time = time.time()
    bubble_operations = bubble_sort(arr.copy())
    bubble_time = time.time() - start_time
    results.append(("Bubble Sort", bubble_operations, bubble_time))

    start_time = time.time()
    insertion_operations = insertion_sort(arr.copy())
    insertion_time = time.time() - start_time
    results.append(("Insertion Sort", insertion_operations, insertion_time))

    start_time = time.time()
    selection_operations = selection_sort(arr.copy())
    selection_time = time.time() - start_time
    results.append(("Selection Sort", selection_operations, selection_time))

    start_time = time.time()
    comb_operations = comb_sort(arr.copy())
    comb_time = time.time() - start_time
    results.append(("Comb Sort", comb_operations, comb_time))

    start_time = time.time()
    shell_operations = shell_sort(arr.copy())
    shell_time = time.time() - start_time
    results.append(("Shell Sort", shell_operations, shell_time))

    # Sortowanie wyników od najwolniejszego do najszybszego
    results.sort(key=lambda x: x[2], reverse=True)

    # Wyświetlenie posortowanych wyników
    print(f"\nRozmiar tablicy z danymi: {size}")
    for result in results:
        print(f"{result[0]}: liczba operacji: {result[1]}, czas: {result[2]:.25f} sekund")
