from random import choice

choices = ['A', 'B', 'C', 'D', 'E', '0', '1',
           '2', '3', '4', '5', '6', '7', '8', '9']


print("Ball's rolling..")


def get_winning_ticket(choices):
    winning_ticket = []

    while len(winning_ticket) < 4:
        item = choice(choices)

        if item not in winning_ticket:
            winning_ticket.append(item)

    return winning_ticket


def random_ticket(choices):
    ticket = []
    while len(ticket) < 4:
        item = choice(choices)

        if item not in ticket:
            ticket.append(item)

    return ticket


def check_ticket(ticket, winning_ticket):
    for element in ticket:
        if element not in winning_ticket:
            return False
    return True


winning_ticket = get_winning_ticket(choices)
plays = 0
max_tries = 1_000_000
won = False

while not won:
    ticket = random_ticket(choices)
    won = check_ticket(ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {ticket}")
    print(f"Winning ticket: {winning_ticket}")
