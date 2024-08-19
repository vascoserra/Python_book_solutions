from random import choice

list = ['A', 'B', 'C', 'D', 'E', '0', '1',
        '2', '3', '4', '5', '6', '7', '8', '9']

choice_1 = choice(list)
list.remove(choice_1)
choice_2 = choice(list)
list.remove(choice_2)
choice_3 = choice(list)
list.remove(choice_3)
choice_4 = choice(list)

print(
    f"The ticket with : '{choice_1}' '{choice_2}' '{choice_3}' '{choice_4}' won!")
