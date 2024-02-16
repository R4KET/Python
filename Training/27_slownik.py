#alien_0 = {'color': 'green', 'points': 5} # słownik

#print(alien_0['color']) # wyświetla wartość z klucza 'color'
#print(alien_0['points']) # wyświetla wartość z klucza 'points'

#alien_0['x_position'] = 0 # dodanie nowego klucza 'x_position' i przypisanie mu wartości 0
#alien_0['y_position'] = 25 # dodanie nowego klucza 'y_position' i przypisanie mu wartości 25
#print(alien_0) # wyświetlenie słownika



#new_points = alien_0['points'] # przypisanie wartości z klucza 'points' do zmiennej
#print("Zarobiłeś " + str(new_points) + " punktów!") # wyświetlenie wartości zmiennej

#alien_0 = {}; # pusty słownik
#alien_0['color'] = 'zielony' # dodanie klucza 'color' i przypisanie mu wartości 'zielony'
#print(f"Kolor obcego to {alien_0['color']}")
#alien_0['points'] = 5 # dodanie klucza 'points' i przypisanie mu wartości 5

#print(alien_0) # wyświetlenie słownika

#alien_0['color'] = 'żółty' # zmiana wartości klucza 'color' na 'żółty'
#print(f"Kolor obcego to {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'średnio'} # słownik z trzema kluczami i wartościami
print(f"Poczatkowa wartosc x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'wolno':
    x_increment = 1 # zmienna x_increment ma wartość 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2 # zmienna x_increment ma wartość 2
else:
    x_increment = 3;

alien_0['x_position'] = alien_0['x_position'] + x_increment # do wartości klucza 'x_position' dodajemy wartość zmiennej x_increment (1, 2 lub 3)
print(f"Nowa wartosc x-position: {alien_0['x_position']}")