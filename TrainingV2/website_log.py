current_users = ['jane', 'lucille', 'jake', 'adam', 'john']
new_users = ['jack', 'matt', 'adam', 'philip']

for new_user in new_users:
    if new_user in current_users:
        print(f"The username: {new_user} is taken.")
    else:
        print(f"The username: {new_user} is available.")