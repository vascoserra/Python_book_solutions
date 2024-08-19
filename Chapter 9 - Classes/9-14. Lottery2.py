from random import choice

choises = ['A', 'B', 'C', 'D', 'E', '0', '1',
           '2', '3', '4', '5', '6', '7', '8', '9']

winning_ticket = []
print("Ball's rolling..")

while len(winning_ticket) < 4:
    item = choice(choises)

    if item not in winning_ticket:
        print(f"We pulled a {item}!")
        winning_ticket.append(item)

print(f"The final result is: {winning_ticket}")
