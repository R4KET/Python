### ZADANIE 2 ###

# A) Funkcja znajdująca największy element w ciągu liczb rzeczywistych:
def find_max(numbers):
    max_number = float('-inf')  # Początkowa wartość największej liczby
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Złożoność obliczeniowa tej funkcji wynosi O(n), gdzie n to liczba elementów w ciągu liczb rzeczywistych. 
# Algorytm przechodzi przez każdy element ciągu raz, aby znaleźć największy element.

# B) Złożoność funkcji sortującej metodą Quick Sort:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Złożoność obliczeniowa algorytmu sortującego Quick Sort to w przypadku średnim O(nlogn). 
# W najgorszym przypadku (gdy pivot jest zawsze minimum lub maksimum) może być O(n2). 
# Jest to efektywny algorytm sortowania, który działa w średnim przypadku szybko, ale zawsze należy uwzględniać potencjalny najgorszy przypadek.

### ZADANIE 5 ###

# w ogólnym przypadku, nie jest możliwe stworzenie algorytmu sortowania o złożoności O(n) dla dowolnego zbioru liczb, w tym dla zbioru odwrotnie posortowanych. 
# Większość algorytmów sortowania, takich jak sortowanie przez mergeSort, quickSort czy insertionSort, mają w najlepszym przypadku złożoność O(nlogn). 
# To dlatego, że sortowanie w swojej zasadzie dzialania wymaga porównywania elementów ze sobą, a liczba tych porównań w zbiorze o n elementach jest typowo proporcjonalna do nlogn.