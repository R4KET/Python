numbers = list(range(1,10))
print(numbers)

for number in numbers:
    if number == 1:
        print("1st\n")
    elif number == 2:
        print("2nd\n")
    elif number == 3:
        print("3rd\n")
    else:
        print(f"{number}th\n")