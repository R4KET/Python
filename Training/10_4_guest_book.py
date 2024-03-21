file = 'guest_book.txt'

while True:
    choice = input("Do you wish to sign the guest book? (yes/no) ")

    if choice == 'yes':
        name = input("Enter your name: ")
        with open(file, 'a') as file_object:
            file_object.write(name + '\n')
    else:
        break