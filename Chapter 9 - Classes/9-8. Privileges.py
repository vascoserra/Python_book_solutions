class User:
    def __init__(self, first_name, last_name, age, sex):
        """Atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def greet_user(self):
        """Greeting user"""
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}!")

    def describe_user(self):
        """Describing users"""
        print("Here are your informations:")
        print(f"Your age is :{self.age}\nYour sex is: {self.sex}\n")

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_attempts += 1
        print(f"You login {self.login_attempts} times.")

    def reset_login_attempts(self):
        """Set login attempts to 0"""
        self.login_attempts = 0
        print(f"You reseted you loggin attempts to {self.login_attempts}")


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("\nThe Admin has these privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin('admin', 'silva', '27', 'Male')
admin.greet_user()
admin.privileges.show_privileges()
