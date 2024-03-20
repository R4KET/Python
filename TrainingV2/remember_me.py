import json


def greet_user():
    """Greet the user by name."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Whats your name? ")
        with open(filename, 'w') as f:
            json.dump(username,f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
        
greet_user()


#username = input("Whats your name? ")

#filename = 'username.json'
#with open(filename,'w') as f:
#    json.dump(username,f)
#    print(f"We'll remember you when you come back, {username}!")