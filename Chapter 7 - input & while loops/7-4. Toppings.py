prompt = "Write 'quit' to exit! \nChoose the toppings for your pizza:"

while True:
    message = input(prompt)
    if message != 'quit':
        print(f"Adding {message} to your pizza!\n")
    else:
        break
