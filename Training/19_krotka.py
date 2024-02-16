dimensions = (200, 50)
print("Wymiary poczatkowe:")
for dimension in dimensions:
    print(dimension)
# dimensions[0] = 250 # nie mozna zmienic wartosci krotki, ERROR


dimensions = (400, 100)
print("\nWymiary po modyfikacji:")
for dimension in dimensions:
    print(dimension)

menu = ('pizza', 'spaghetti', 'lasagne', 'pierogi', 'sushi')
print("\nMenu restauracji:")
for dish in menu:
    print(dish)

menu = ('pizza', 'spaghetti', 'lasagne', 'chicken', 'burger')
print("\nNowe menu restauracji:")
for dish in menu:
    print(dish)
