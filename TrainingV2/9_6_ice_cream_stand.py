class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The new restaurant is open!")
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"The restaurant's makes {self.cuisine_type} food.")

    def customers(self):
        print(f"The restaurant has served {self.number_served} customers.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in flavors:
            print(f"{flavor.title()}")

flavors = ["chocolate", "strawberry", "blueberry"]

my_icecream_stand = IceCreamStand("Watermelon", "Orange", flavors)
my_icecream_stand.display_flavors()
print("-----------")
my_icecream_stand.flavors.extend(["Watermelon", "Orange"])
my_icecream_stand.display_flavors()

#restaurant = Restaurant('Lucky', 'Chinese')
#restaurant.describe_restaurant()
#restaurant.customers()
#restaurant.set_number_served(10)
#restaurant.customers()
#restaurant.increment_number_served(5)
#restaurant.customers()