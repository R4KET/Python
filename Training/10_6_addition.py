def add_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The sum is:", result)
    except ValueError:
        print("Error: Please enter valid numerical values.")

add_numbers()
