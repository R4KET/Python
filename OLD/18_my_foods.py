my_foods = ['pizza', 'falafel', 'carrot cake', 'spaghetti', 'lasagne', 'pierogi', 'sushi', 'pasta', 'chicken', 'burger']
friend_foods = my_foods[:] # kopiowanie listy

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Moje ulubione potrawy to:")
print(my_foods)

print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_foods)

print("\nPierwsze trzy potrawy z mojej listy to:")
print(my_foods[:3])

print("\nTrzy potrawy z srodka listy to:")
print(my_foods[4:7])

print("\nOstatnie trzy potrawy z listy to:")
print(my_foods[-3:])