file = 'poll.txt'

while True:
    choice = input("Do you wish to attempt to the programming poll? (yes/no) ")

    if choice == 'yes':
        name = input("Enter your name: ")
        reason = input("What's the reason you like to program? ")
        with open(file, 'a') as file_object:
            file_object.write(name.title() + ' - ' + reason + '\n')
    else:
        break