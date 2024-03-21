sandwich_orders = [
    "The Classic Club",
    "Veggie Delight",
    "Turkey Avocado Bliss",
    "Spicy Chicken Ranch",
    "Italian Stallion",
    "The Ultimate Reuben"
]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)