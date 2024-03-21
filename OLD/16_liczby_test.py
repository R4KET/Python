liczby = []
for value in range(1, 1000001):
    liczby.append(value)

print(liczby[2136])

print(min(liczby))
print(max(liczby))
print(sum(liczby))

nieparzyste = []
for value in range(1, 21, 2):
    nieparzyste.append(value)

print(nieparzyste)

trzy = []
for value in range(3, 31):
    trzy.append(value**3)

print(trzy)

# Tworzenie listy sześcianów
szesciany = [i ** 3 for i in range(1, 11)]

# Wyświetlanie sześcianów za pomocą pętli for
for szescian in szesciany:
    print(szescian)
