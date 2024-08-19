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


restaurant_one = Restaurant('Makisushi', 'sushi', )
print(f"The restaurant name is {restaurant_one.restaurant_name}")
print(f"The cuisine type is {restaurant_one.cuisine_type}")
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two = Restaurant('Sushitoro', 'chinese')
print(f"\nThe restaurant name is {restaurant_two.restaurant_name}")
print(f"The cuisine type is {restaurant_two.cuisine_type}")
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('Kai-Fu', 'sushi and chinese')
print(f"\nThe restaurant name is {restaurant_three.restaurant_name}")
print(f"The cuisine type is {restaurant_three.cuisine_type}")
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()


restaurant = Restaurant('Cantinho do Avilez', 'Comida tipica portuguesa')
restaurant.increment_number_served(3)
