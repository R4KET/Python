number = input("Tell me your lucky number: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} can be multiplied by ten.")
else:
    print(f"The number {number} cannot be multiplied by ten.")