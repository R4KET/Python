class Kolejka:
    def __init__(self):
        self.kolejka = []

    def is_empty(self):
        return len(self.kolejka) == 0

    def enqueue(self, element):
        self.kolejka.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.kolejka.pop(0)
        else:
            return None

    def UsunX(self, x):
        if x in self.kolejka:
            self.kolejka.remove(x)

# 1. Funkcja StosL
def StosL(elStosu, stos):
    for num in elStosu:
        if num % 3 == 0 and num != 0:
            stos.append(num)

# 2. Funkcja do obracania stosu przy użyciu drugiego stosu
def ObracanieStosu(stos):
    stos.reverse()

# 3. Funkcja do usunięcia elementu na pozycji n
def usunN(stos, n):
    if n > len(stos):
        print("Błąd: stos jest za krótki.")
        return
    stos.pop(n - 1)

# 4. Funkcja do łączenia dwóch list
def PolaczListy(lista1, lista2):
    lista1 += lista2
    lista2.clear()

# 5. Funkcja do usunięcia elementu o wartości X
def usunX(kolejka, x):
    kolejka.UsunX(x)

# Przykładowe użycie funkcji
elStosu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stos = []
print("Stos początkowy: ", stos)
print("Stos po wstawieniu elementów: ", elStosu)
StosL(elStosu, stos)
print("Zawartość stosu po StosL: ", stos)
print("----------------------------------------")

stos = elStosu.copy()  # kopiowanie stosu
ObracanieStosu(stos)
print("Zawartość stosu po ObracanieStosu: ", stos)
print("----------------------------------------")

stos = elStosu.copy()  # kopiowanie stosu
usunN(stos, 4)
print("Po usunięciu elementu n: ", stos)
print("----------------------------------------")

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]
PolaczListy(lista1, lista2)
print("Zawartość listy po PolaczListy:", lista1)
print("Lista 2: ")
print("----------------------------------------")

kolejka = Kolejka()
kolejka.enqueue(1)
kolejka.enqueue(2)
kolejka.enqueue(3)
kolejka.enqueue(4)
kolejka.enqueue(5)

element_do_usuniecia = 3
usunX(kolejka, element_do_usuniecia)
print("Kolejka po usunięciu elementu", element_do_usuniecia, ":", kolejka.kolejka)

element_do_usuniecia = 6  # Element, który nie istnieje w kolejce
usunX(kolejka, element_do_usuniecia)
print("Kolejka po próbie usunięcia elementu", element_do_usuniecia, ":", kolejka.kolejka)
