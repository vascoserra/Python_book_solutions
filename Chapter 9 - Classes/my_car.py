from car import Car, Eletric_car, Battery

my_tesla = Car('Tesla', 'Model S', 2022)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 150
my_tesla.read_odometer()
my_tesla = Eletric_car('Tesla', 'Model S', '2023')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
