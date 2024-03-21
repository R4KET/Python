pizzas = ['pepperoni', 'hawajska', 'margarita']
for pizza in pizzas:
    print(f"Lubie pizze {pizza}")

print("Naprawde lubie pizze!")

friend_pizzas = pizzas[:]
friend_pizzas.append('wegetarianska')

print("\nMoje ulubione pizze to:")
for pizza in pizzas:
    print(pizza)    

print("\nUlubione pizze mojego przyjaciela to:")
for pizza in friend_pizzas:
    print(pizza)