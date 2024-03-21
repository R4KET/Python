sandwich_orders = [
    "The Classic Club",
    "Pastrami",
    "Veggie Delight",
    "Turkey Avocado Bliss",
    "Spicy Chicken Ranch",
    "Italian Stallion",
    "Pastrami",
    "The Ultimate Reuben",
    "Pastrami"
]

# print(sandwich_orders)

finished_sandwiches = []

print("\nThe deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)