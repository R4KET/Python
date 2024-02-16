def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        # Zamiana elementów
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Zamiana: {arr[i]} i {arr[largest]}")
        
        # Rekurencyjne wywołanie na zmienionym poddrzewie
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Budowa kopca
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Wyodrębnianie elementów z kopca
    for i in range(n - 1, 0, -1):
        # Zamiana korzenia z ostatnim elementem
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Zamiana: {arr[i]} i {arr[0]}")
        
        # Wywołanie rekurencyjne na zmniejszonym kopcu
        heapify(arr, i, 0)

# Przykładowe dane do posortowania
data = [4, 26, 19, 60, -3, 32, 38, 18, 92]

# Wywołanie sortowania przez kopcowanie
heapSort(data)

# Wynik posortowania
print("Posortowane dane:", data)

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid  # Znaleziono element x na pozycji mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element x nie istnieje w tablicy

# Przykładowa posortowana tablica
sorted_array = data

# Element do wyszukania
x = 32

# Wywołanie funkcji do wyszukiwania
result = binary_search(sorted_array, x)

if result != -1:
    print(f"Element {x} znajduje się na pozycji {result}.")
else:
    print(f"Element {x} nie istnieje w tablicy.")

