import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = random.randint(1, self.sides)
        print(f"The die rolls: {roll}")

six_sided_die = Die()

print("Rolling the 6-sided die 10 times:")
for x in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)

print("Rolling the 10-sided die 10 times:")
for x in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)

print("Rolling the 20-sided die 10 times:")
for x in range(10):
    twenty_sided_die.roll_die()