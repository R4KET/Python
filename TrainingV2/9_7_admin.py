class User:

    def __init__(self, first_name, last_name, login, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.date_of_birth = date_of_birth
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's name is {self.first_name}")
        print(f"The user's last name is {self.last_name}")
        print(f"The user's login is {self.login}")
        print(f"The user's date of birth is {self.date_of_birth}")

    def attempts(self):
        print(f"{self.login} attempted to login {self.login_attempts} times.")

    def increment_login_attempt(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):

    def __init__(self, first_name, last_name, login, date_of_birth, privileges):
        super().__init__(first_name, last_name, login, date_of_birth)
        self.privileges = Privileges(privileges)

    def describe_user(self):
        super().describe_user()
    
class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

privileges = ["can add post", "can delete post", "can ban user"]
admin = Admin("Adam", "Lopez", "SuperAdmin", "11-11-1985", privileges)
admin.describe_user()
admin.privileges.show_privileges()

#user = User("John", "Kicinsky", "JK2137", "10-10-1991")
#user.describe_user()
#user.attempts()
#user.increment_login_attempt()
#user.attempts()
#user.reset_login_attempts()
#user.attempts()