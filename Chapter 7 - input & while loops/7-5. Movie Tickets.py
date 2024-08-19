prompt = "\nEnter quit to exit! \nWhats is your age?: "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Your ticket its free!")
    elif age < 12:
        print("Your ticket its 10$!")
    else:
        print("Your ticket its 15$!")
