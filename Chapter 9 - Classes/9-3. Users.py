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


me = User('nuno', 'silva', '27', 'Male')
me.greet_user()
me.describe_user()

joana = User('joana', 'soares', '26', 'Feminine')
joana.greet_user()
joana.describe_user()

me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()

me.reset_login_attempts()
