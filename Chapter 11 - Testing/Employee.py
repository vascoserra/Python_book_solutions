class Employe:
    def __init__(self, first_name, last_name, salary=10000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def description(self):
        print(f"{self.first_name} {self.last_name} salary is -> {self.salary}!")

    def give_raise(self, raisee=5000):
        self.salary += raisee


nuno = Employe('Nuno', 'Silva')
nuno.description()
nuno.give_raise(10000)
nuno.description()
