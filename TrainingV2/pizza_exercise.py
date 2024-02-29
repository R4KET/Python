my_pizzas = ['Parma', 'Hawaiian', 'Margheritta']
friend_pizzas = my_pizzas[:]

my_pizzas.append("Bolivia")
friend_pizzas.append("Mexicana")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("-------")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)