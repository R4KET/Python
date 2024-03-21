cars = ['subaru', 'jeep', 'skoda', 'ford']
requested_car = input("What car are you looking for? ").lower()

if requested_car in cars:
    print(f"We've got the {requested_car.title()} you're looking for.")
else:
    print(f"Sorry, we do not have a {requested_car.title()}")