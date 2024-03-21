file = 'guest_name.txt'

name = input("Enter your name:")

with open(file, 'a') as file_object:
    file_object.write(name + '\n')