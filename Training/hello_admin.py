names = ['jane', 'lucille', 'jake', 'adam', 'john', 'admin']

if names == []:
    print("We need to add users!")
else:
    if 'admin' in names:
        print("Hello admin, would you like to see a status report?")
    else:
        for name in names:
            print(f"Hello {name.title()}, thank you for logging in again.")