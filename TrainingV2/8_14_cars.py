def car(make, model, **kwargs):
    """Building a dictionary containing everything we know about a user."""
    kwargs['make'] = make
    kwargs['model'] = model
    return kwargs

car1 = car('Jeep', 'Grand Cherokee', type="Offroad", engine='5.9L')
car2 = car('Ford', 'Escort', type="Sedan", engine='1.3L')
print(car1)
print(car2)