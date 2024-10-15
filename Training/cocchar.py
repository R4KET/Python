import random
import math

def rzut_koscia(typ_kosci, liczba_rzutow):
    return sum(random.randint(1, typ_kosci) for _ in range(liczba_rzutow))

def modyfikator_obrazen_i_krzepa(sila, budowaCiala):
    suma = sila + budowaCiala
    
    if 2 <= suma <= 64:
        modyfikator_obrazen = -2
        krzepa = -2
    elif 65 <= suma <= 84:
        modyfikator_obrazen = -1
        krzepa = -1
    elif 85 <= suma <= 124:
        modyfikator_obrazen = 0
        krzepa = 0
    elif 125 <= suma <= 164:
        modyfikator_obrazen = '+1K4'
        krzepa = 1
    elif 165 <= suma <= 204:
        modyfikator_obrazen = '+1K6'
        krzepa = 2
    elif 205 <= suma <= 284:
        modyfikator_obrazen = '+2K6'
        krzepa = 3
    elif 285 <= suma <= 364:
        modyfikator_obrazen = '+3K6'
        krzepa = 4
    elif 365 <= suma <= 444:
        modyfikator_obrazen = '+4K6'
        krzepa = 5
    elif 445 <= suma <= 524:
        modyfikator_obrazen = '+5K6'
        krzepa = 6
    else:
        # Dla każdej kolejnej wartości powyżej 524, dodaj 1K6 do obrażeń i 1 do krzepy
        dodatkowe = (suma - 445) // 80
        modyfikator_obrazen = f'+{5 + dodatkowe}K6'
        krzepa = 6 + dodatkowe

    return modyfikator_obrazen, krzepa

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
punktyWytrzymalosci = math.floor((kondycja + budowaCiala)/5)
punktyMagii = moc * 1/5

if zrecznosc < budowaCiala and sila < budowaCiala:
    zakresRuchu = 7
elif (zrecznosc >= budowaCiala or sila >= budowaCiala) or (zrecznosc == budowaCiala and sila == budowaCiala):
    zakresRuchu = 8
elif zrecznosc > budowaCiala and sila > budowaCiala:
    zakresRuchu = 9
else:
    zakresRuchu = 0  # Opcjonalnie, gdyby nie spełniono żadnego z warunków

modyfikatorObrazen, krzepa = modyfikator_obrazen_i_krzepa(sila, budowaCiala)

print("Cechy: ")
print(f"Siła: {sila}")
print(f"Kondycja: {kondycja}")
print(f"Budowa Ciała: {budowaCiala}")
print(f"Zręczność: {zrecznosc}")
print(f"Wygląd: {wyglad}")
print(f"Inteligencja: {inteligencja}")
print(f"Moc: {moc}")
print(f"Wykształcenie: {wyksztalcenie}")
print("---------------------")
print(f"Szczęście: {szczescie}")
print(f"Punkty Poczytalności: {punktyPoczytalnosci}")
print(f"Punkty Wytrzymałości: {punktyWytrzymalosci}")
print(f"Punkty Magii: {punktyMagii}")
print(f"Modyfikator obrażeń: {modyfikatorObrazen}, Krzepa: {krzepa}")
print(f"Zakres Ruchu: {zakresRuchu}")