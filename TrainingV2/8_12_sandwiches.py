def make_sadnwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sadnwich('ham')
make_sadnwich('cheese', 'ham', 'lettuce')
make_sadnwich('ham', 'lettuce')
make_sadnwich('cheese', 'chicken', 'ketchup', 'garlic', 'mustard')