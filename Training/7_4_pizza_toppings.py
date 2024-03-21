toppings = []

print("Enter the toppings you want on your pizza:")
print("(Enter 'quit' when you are finished)")

while True:
    topping = input("Add a topping: ")

    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Here's your pizza with the toppings: {toppings}")

print(f"The pizza with {', '.join(toppings)} will be ready in a moment.")