import random

class Klient:
    def __init__(self, imie, wiek, zarobki):
        self.imie = imie
        self.wiek = wiek
        self.zarobki = zarobki

class Kolejka:
    def __init__(self):
        self.kolejka = []

    def dodaj(self, element):
        self.kolejka.append(element)

    def usun(self):
        if self.kolejka:
            return self.kolejka.pop(0)
        else:
            return None

    def __len__(self):
        return len(self.kolejka)
    

def srednie_zarobki(bank):
    return sum([klient.zarobki for klient in bank.kolejka]) / len(bank)

def przedzial_zarobkow(bank, min_zarobki, max_zarobki):
    klienci_w_przedziale = [klient for klient in bank.kolejka if min_zarobki <= klient.zarobki <= max_zarobki]
    print("Klienci w przedziale zarobków od: " + str(min_zarobki) + "zł do " + str(max_zarobki) + "zł:")
    for klient in klienci_w_przedziale:
        print(f"Imię: {klient.imie}, Zarobki: {klient.zarobki}")

def update_client(bank, index, nowe_imie, nowy_wiek, nowe_zarobki):
    if index < len(bank):
        bank.kolejka[index] = Klient(nowe_imie, nowy_wiek, nowe_zarobki)
        print(f"Klient na pozycji {index} został zaktualizowany.")
        print(f"Nowe imie: " + bank.kolejka[index].imie + ", nowy wiek: " + str(bank.kolejka[index].wiek) + ", nowe zarobki: " + str(bank.kolejka[index].zarobki) + "zł.")
    else:
        print("Nie ma klienta na podanej pozycji.")

bank = Kolejka()

# symulacja dodawania klientow, poczatek kolejki
for _ in range(20):
    if random.random() < 0.5:
        imie = "Klient: " + str(len(bank.kolejka) + 1)
        wiek = random.randint(18, 70)
        zarobki = random.randint(1000, 10000)
        klient = Klient(imie, wiek, zarobki)
        bank.kolejka.insert(0, klient)

# papierkowa robota, koniec kolejki
for _ in range(20):
    if random.random() < 0.25:
        imie = "Klient: " + str(len(bank.kolejka) + 1)
        wiek = random.randint(18, 70)
        zarobki = random.randint(1000, 10000)
        klient = Klient(imie, wiek, zarobki)
        bank.dodaj(klient)

print("Średnie zarobki " + str(len(bank)) + " klientów wynoszą: " + str((round(srednie_zarobki(bank),2))) + "zł.")

przedzial_zarobkow(bank, 2500, 5000)

update_client(bank, 4, "NoweImie", 25, 6000)