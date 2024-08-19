current_users = ['nuno', 'joana', 'xana', 'nina', 'jose']
new_users = ['nuno', 'nina', 'goncalo', 'tiago', 'rebeca']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} has been taken, choose another name!")
    else:
        current_users.append(new_user)
        print(f"{new_user} is now on current users")
print(current_users)
