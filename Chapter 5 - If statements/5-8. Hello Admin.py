# usernames = ['admin', 'nuno', 'joana', 'nina', 'xana']
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, it's good to see you again!")
else:
    print("We need some users first!")
