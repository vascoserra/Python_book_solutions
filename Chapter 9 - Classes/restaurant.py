class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Iniciate atributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describing the restaurant"""
        print(f"{self.restaurant_name.title()}'s is a {self.cuisine_type.title()} local restaurant with fresh products.")

    def open_restaurant(self):
        """What times does restaurant Opens"""
        print(f"{self.restaurant_name.title()}'s opens at 12:00")

    def set_number_served(self, people_served):
        """Print the number os people served"""
        self.number_served = people_served
        print(
            f"Today {self.restaurant_name.title()} served {self.number_served} people.")

    def increment_number_served(self, increment):
        """Increment people served"""
        self.number_served += increment
        print(f"Today we served more {self.number_served} people.")
