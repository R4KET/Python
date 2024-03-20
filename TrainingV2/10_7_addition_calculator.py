def add_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("The sum is:", result)
            break  # Exit the loop if input is successfully converted to numbers
        except ValueError:
            print("Error: Please enter valid numerical values.")

add_numbers()
