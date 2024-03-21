while True:
    age_input = input("How old are you? ")
    if age_input.lower() == 'quit':
        break

    age = int(age_input)

    if age <= 3:
        print("The ticket price is 0$.")
    elif 3 < age <= 12:
        print("The ticket price is 10$.")
    else:
        print("The ticket price is 15$.")
