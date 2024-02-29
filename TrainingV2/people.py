person1 = {'name' : 'john', 'age' : 15, 'nationality' : 'english'}
person2 = {'name' : 'adam', 'age' : 19, 'nationality' : 'irish'}
person3 = {'name' : 'anna', 'age' : 17, 'nationality' : 'german'}

frens = [person1, person2, person3]

for friend in frens:
    print(f"Name: {friend['name'].title()}")
    print(f"Age: {friend['age']}")
    print(f"Nationaliy: {friend['nationality'].title()}")
    print("-----------")