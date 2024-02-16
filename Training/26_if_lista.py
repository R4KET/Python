users = ['Admin', 'Krzysiek', 'Ania', 'Kasia', 'Kamil']
for user in users:
    if user == 'Admin':
        print("Witaj Admin, czy chcesz przejrzeć dzisiejszy raport?")
    else:
        print("Witaj " + user + ", dziękujemy, że ponownie się zalogowałeś")

users2 = ['Admin', 'Krzysiek', 'Ania', 'Kasia', 'Kamil'];
if users2 == []:
    print("Musimy znaleźć jakichś użytkowników!")
else:
    print("Mamy " + str(len(users2)) + " użytkowników!")


current_users = ['Admin', 'Krzysiek', 'Ania', 'Kasia', 'Kamil']
new_users = ['Janek', 'Marek', 'Ania']
for new_user in new_users:
    if new_user in current_users:
        print("Nazwa użytkownika " + new_user + " jest już zajęta, podaj inną nazwę")
    else:
        print("Nazwa użytkownika " + new_user + " jest dostępna")