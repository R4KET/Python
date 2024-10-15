import random
import math

# Funkcja rzutu kostką
def rzut_koscia(typ_kosci, liczba_rzutow):
    return sum(random.randint(1, typ_kosci) for _ in range(liczba_rzutow))

# Funkcja obliczania modyfikatora obrażeń i krzepy
def modyfikator_obrazen_i_krzepa(sila, budowaCiala):
    suma = sila + budowaCiala
    
    if 2 <= suma <= 64:
        return -2, -2
    elif 65 <= suma <= 84:
        return -1, -1
    elif 85 <= suma <= 124:
        return 0, 0
    elif 125 <= suma <= 164:
        return '+1K4', 1
    elif 165 <= suma <= 204:
        return '+1K6', 2
    elif 205 <= suma <= 284:
        return '+2K6', 3
    elif 285 <= suma <= 364:
        return '+3K6', 4
    elif 365 <= suma <= 444:
        return '+4K6', 5
    elif 445 <= suma <= 524:
        return '+5K6', 6
    else:
        dodatkowe = (suma - 445) // 80
        return f'+{5 + dodatkowe}K6', 6 + dodatkowe

# Funkcja obliczania zakresu ruchu
def oblicz_zakres_ruchu(zrecznosc, sila, budowaCiala):
    if zrecznosc < budowaCiala and sila < budowaCiala:
        return 7
    elif zrecznosc > budowaCiala and sila > budowaCiala:
        return 9
    else:
        return 8

# Funkcja generowania cech postaci
def generuj_cechy():
    sila = rzut_koscia(6, 3) * 5
    kondycja = rzut_koscia(6, 3) * 5
    budowaCiala = (rzut_koscia(6, 2) + 6) * 5
    zrecznosc = rzut_koscia(6, 3) * 5
    wyglad = rzut_koscia(6, 3) * 5
    inteligencja = (rzut_koscia(6, 2) + 6) * 5
    moc = rzut_koscia(6, 3) * 5
    wyksztalcenie = (rzut_koscia(6, 2) + 6) * 5
    szczescie = (rzut_koscia(6, 2) + 6) * 5
    
    punktyPoczytalnosci = moc
    punktyWytrzymalosci = math.floor((kondycja + budowaCiala) / 5)
    punktyMagii = moc // 5
    
    modyfikatorObrazen, krzepa = modyfikator_obrazen_i_krzepa(sila, budowaCiala)
    zakresRuchu = oblicz_zakres_ruchu(zrecznosc, sila, budowaCiala)

    # Zwracamy wszystkie cechy w formie słownika
    return {
        "sila": sila, "kondycja": kondycja, "Budowa Ciała": budowaCiala, "zrecznosc": zrecznosc,
        "wyglad": wyglad, "inteligencja": inteligencja, "moc": moc, "wyksztalcenie": wyksztalcenie,
        "szczescie": szczescie, "Punkty Poczytalności": punktyPoczytalnosci, "Punkty Wytrzymałości": punktyWytrzymalosci,
        "Punkty Magii": punktyMagii, "Modyfikator Obrażeń": modyfikatorObrazen, "krzepa": krzepa,
        "Zakres Ruchu": zakresRuchu
    }

# Generowanie cech postaci
cechy = generuj_cechy()

# Wypisanie cech
print("Cechy: ")
for cecha, wartosc in cechy.items():
    print(f"{cecha.title()}: {wartosc}")
