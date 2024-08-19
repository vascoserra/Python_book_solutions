filename = 'guest_book.txt'

print("To stop write quit!")
while True: 
    guest = input("Whats your name? ")
    if guest == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{guest}\n")
        print(f"{guest} you have been added to guestlist!")