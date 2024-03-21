guests = ['John', 'Amarie', 'Adam', 'Jake', 'Lucille']
print(f"I'd like to invite you to a dinner {guests[0].title()}")
print(f"I'd like to invite you to a dinner {guests[1].title()}")
print(f"I'd like to invite you to a dinner {guests[2].title()}")
print(f"I'd like to invite you to a dinner {guests[3].title()}")
print(f"I'd like to invite you to a dinner {guests[4].title()}")

print("------------")

cannot_come = 'Adam'
forgot_to_invite = 'Matt'
guests.remove(cannot_come)
guests.append(forgot_to_invite)
print(f"I'd like to invite you to a dinner {guests[0].title()}")
print(f"I'd like to invite you to a dinner {guests[1].title()}")
print(f"I'd like to invite you to a dinner {guests[2].title()}")
print(f"I'd like to invite you to a dinner {guests[3].title()}")
print(f"I'd like to invite you to a dinner {guests[4].title()}")

guests.append('Hal')
guests.append('Bjorn')
guests.append('Thomas')

print("------------")
print(f"I'd like to invite you to a dinner {guests[0].title()}")
print(f"I'd like to invite you to a dinner {guests[1].title()}")
print(f"I'd like to invite you to a dinner {guests[2].title()}")
print(f"I'd like to invite you to a dinner {guests[3].title()}")
print(f"I'd like to invite you to a dinner {guests[4].title()}")
print(f"I'd like to invite you to a dinner {guests[5].title()}")
print(f"I'd like to invite you to a dinner {guests[6].title()}")
print(f"I'd like to invite you to a dinner {guests[7].title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
no_space = guests.pop()
print(f"Sorry, but there's not enough space {no_space.title()}")
print(guests)
del guests[1]
del guests[0]

print(guests)