message = "Hello world"
print(message)

message = "Hello world 2"
print(message)
print(message)

import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Generowanie losowej listy
losowa_lista = [random.randint(1, 100) for _ in range(10)]  # Zmiana liczby "10" na żądaną długość listy

print("Wygenerowana lista:", losowa_lista)

# Sortowanie bąbelkowe
posortowane_babelkowe = bubble_sort(losowa_lista.copy())
print("Sortowanie bąbelkowe:", posortowane_babelkowe)

# Sortowanie szybkie
posortowane_szybkie = quick_sort(losowa_lista.copy())
print("Szybkie sortowanie:", posortowane_szybkie)
