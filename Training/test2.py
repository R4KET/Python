import random
import timeit

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
        mniejsze = [x for x in lista[1:] if x <= pivot]
        wieksze = [x for x in lista[1:] if x > pivot]
        return quick_sort(mniejsze) + [pivot] + quick_sort(wieksze)
    
def hybrid_sort(lista):
    if len(lista) <= 100:
        return bubble_sort(lista)
    elif len(lista) > 100 and len(lista) < 10000:
        return quick_sort(lista)
    else:
        return sorted(lista)
    
def compare_algorithms(lista):
    start_time = timeit.default_timer()
    sorted_bubble = bubble_sort(lista.copy())
    bubble_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_quick_sort = quick_sort(lista.copy())
    quick_sort_time = timeit.default_timer() - start_time

    start_time = timeit.default_timer()
    sorted_hybrid_sort = hybrid_sort(lista.copy())
    hybrid_sort_time = timeit.default_timer() - start_time

    print("Czas sortowania bąbelkowego:", bubble_time)
    print("Czas sortowania QuickSort:", quick_sort_time)
    print("Czas sortowania hybrydowego:", hybrid_sort_time)

#losowa_lista = [random.randint(1, 100) for _ in range(10000)]
#
#print("Wygenerowana lista:", losowa_lista)
#print("--------------------------")
#posortowane_babelkowe = bubble_sort(losowa_lista.copy())
#print("Sortowanie bąbelkowe:", posortowane_babelkowe)
#print("--------------------------")
#posortowane_szybkie = quick_sort(losowa_lista.copy())
#print("Szybkie sortowanie:", posortowane_szybkie)

#compare_algorithms(losowa_lista)

print("-------------------------------------")
print("Dla zbioru danych mniejszego lub rownego 100 jest wybierane sortowanie babelkowe")
print("Dla zbioru danych wiekszego od 100 lecz mniejszeo niz 10000 wyberany jest QuickSort")
print("Dla zbioru danych wiekszego niz 10000 wybierany jest domyslny algorytm sortowania zaszyty w Pythonie")
print("Wyniki porownujemy dla zbiru danych o wielkosci 100, 1000 i 10000")
print("-------------------------------------")

rozmiary_list = [100, 1000, 10000]
funkcje_sortujace = [bubble_sort, quick_sort, hybrid_sort]

for rozmiar in rozmiary_list:
    print(f"\nRozmiar listy: {rozmiar}")
    losowa_lista = [random.randint(1, 100) for _ in range(rozmiar)]
    
    for funkcja in funkcje_sortujace:
        start_time = timeit.default_timer()
        sorted_list = funkcja(losowa_lista.copy())
        elapsed_time = timeit.default_timer() - start_time
        print(f"Czas sortowania {funkcja.__name__}: {elapsed_time} sekund")