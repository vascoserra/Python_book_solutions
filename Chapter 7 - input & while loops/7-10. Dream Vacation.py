responses = {}
pool_active = True

while pool_active:
    name = input("Whats your name? ")
    vacation = input("What is your dream vacation? ")

    responses[name] = vacation
    repeat = input("Would you like to add someone else? yes/no")
    if repeat == 'no':
        pool_active = False

print("\n---The results are:---")
for name, vacation in responses.items():
    print(f"{name.title()} dream vacation is {vacation.title()}")
