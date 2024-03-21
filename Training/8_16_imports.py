import car_module as cm
import make_sandwich_module as ms

car1 = cm.car('Jeep', 'Grand Cherokee', type="Offroad", engine='5.9L')
car2 = cm.car('Ford', 'Escort', type="Sedan", engine='1.3L')
print(car1)
print(car2)

ms.make_sadnwich('ham')
ms.make_sadnwich('cheese', 'ham', 'lettuce')
ms.make_sadnwich('ham', 'lettuce')
ms.make_sadnwich('cheese', 'chicken', 'ketchup', 'garlic', 'mustard')