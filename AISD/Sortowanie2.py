import random
import timeit

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

# Sortowanie kubełkowe, punkt 1
def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)
    
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Sortowanie niestandardowych danych, punkt 2
class Patient:
    def __init__(self, surname, room_number):
        self.surname = surname
        self.room_number = room_number

def sort_custom_data(data, attribute):
    sorted_data = sorted(data, key=lambda x: getattr(x, attribute))
    return sorted_data

# Sortowanie cząstkowe (Partial Sort), punkt 3
def partial_sort(arr, k):
    return sorted(arr)[:k]

# Hybrydowy algorytm sortowania, punkt 4 - jeżeli zakres jest mniejszy lub równy 10 pracujemy na sortowaniu kubelkowym
# w przeciwnym razie uruchomiony zostaje algorytm sortowania domyślnie zaszyty w Pythonie
def hybrid_sort(arr):
    if len(arr) <= 10:
        return bucket_sort(arr)
    else:
        return sorted(arr)

# Sortowanie w miejscu (In-Place Sorting), punkt 5
def in_place_sort(arr):
    arr.sort()
    return arr

# Porównanie z innymi algorytmami sortowania
def compare_algorithms(arr):
    start_time = timeit.default_timer()
    sorted_arr_bucket = bucket_sort(arr.copy())
    bucket_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_builtin = sorted(arr.copy())
    builtin_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_bubble = bubble_sort(arr.copy())
    bubble_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_shell = shell_sort(arr.copy())
    shell_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_insertion = insertion_sort(arr.copy())
    insertion_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_selection = selection_sort(arr.copy())
    selection_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_arr_comb = comb_sort(arr.copy())
    comb_time = timeit.default_timer() - start_time

    # Porównanie efektywności
    print("Czas sortowania kubełkowego:", bucket_time)
    print("Czas wbudowanego sortowania:", builtin_time)
    print("Czas sortowania bąbelkowego:", bubble_time)
    print("Czas sortowania Shella:", shell_time)
    print("Czas sortowania przez wstawianie:", insertion_time)
    print("Czas sortowania przez wybór:", selection_time)
    print("Czas sortowania grzebieniowego:", comb_time)

# Testowanie algorytmów
data_to_sort = [random.random() for _ in range(10000)]

# Using Patient objects
patients = [Patient(f"Pacjent_{i}", random.randint(1, 100)) for i in range(1, 21)]
sorted_patients = sort_custom_data(patients, "surname")
print("\nSortowanie niestandardowych danych:")
for patient in sorted_patients:
    print(patient.surname, patient.room_number)

partial_first = 10
partial_sorted = partial_sort(data_to_sort, partial_first)
print(f"\nSortowanie {partial_first} pierwszych elementów:")
print(partial_sorted)

hybrid_sorted = hybrid_sort(data_to_sort)
print("\nHybrydowy algorytm sortowania:")
print(hybrid_sorted)

in_place_sorted = in_place_sort(data_to_sort.copy())
print("\nSortowanie w miejscu:")
print(in_place_sorted)

compare_algorithms(data_to_sort)
