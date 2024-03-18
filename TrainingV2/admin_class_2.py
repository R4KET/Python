from user_class import User
from privileges_class import Privileges

class Admin(User):

    def __init__(self, first_name, last_name, login, date_of_birth, privileges):
        super().__init__(first_name, last_name, login, date_of_birth)
        self.privileges = Privileges(privileges)

    def describe_user(self):
        super().describe_user()