sandwich_orders = ['pastrami', 'pita', 'atum',
                   'pastrami', 'mediterranea', 'ovo', 'pastrami']
finished_sandwiches = []

print(sandwich_orders)
print("\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
    print(f"Your {sandwich_order.title()} sandwich in being made!")
    finished_sandwiches.append(sandwich_order)

print("\nWe just made these sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")
