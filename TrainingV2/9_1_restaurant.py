class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The new restaurant is open!")
        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"The restaurant's makes {self.cuisine_type}")

restaurant1 = Restaurant('Lucky', 'Chinese')
restaurant1.describe_restaurant()