#motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

#motorcycles[0] = 'ducati' # change first element
#print(motorcycles)

#motorcycles.append('ducati') # add element to the end of the list
#print(motorcycles)

#motorcycles = [] # create empty list
#motorcycles.append('honda') # add element to the end of the list
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')

#print(motorcycles)

#motorcycles.insert(0, 'ducati') # add element to the beginning of the list
#print(motorcycles) 

#del motorcycles[0] # delete element from the list
#print(motorcycles)

#del motorcycles[-1] # delete last element from the list
#Print(motorcycles)

#popped_motorcycle = motorcycles.pop() # delete last element from the list and assign it to variable
#print(motorcycles)
#print(popped_motorcycle) #  print deleted element

motorcycles = ['honda', 'yamaha', 'suzuki']
#last_owned = motorcycles.pop()
#print(f"Ostatnio zakupiony przeze mnie motocykl to {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"Pierwszy zakupiony przeze mnie motocykl to {first_owned.title()}.")

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nMotocykl {too_expensive.title()} jest zbyt drogi dla mnie.")