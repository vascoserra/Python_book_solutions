my_pizzas = ['Diavola', '4 Queijos', 'Margharitta', 'Pepperonni']
# for pizza in my_pizzas:
#    print(f"This is a {pizza} pizza")
# print(pizzas[:2])
# print(pizzas[1:3])
# print(pizzas[2:])
your_pizzas = my_pizzas[:]
my_pizzas.append('Fungi')
your_pizzas.append('Bacon')
# print(f"My fav pizzas are {my_pizzas} ")
# print(f"Your's fav pizzas are {your_pizzas} ")
for my_pizza in my_pizzas:
    print(f"I love {my_pizza} pizza!!")
for your_pizza in your_pizzas:
    print(f"My friend loves {your_pizza} pizza!!")
