fav_numbers = {
    'nuno': [3, 6, 12],
    'nina': [10],
    'cristiano': [7, 55]
}
# print(f"Nuno favorite number is {fav_numbers['nuno']}")
# print(f"Nina favorite number is {fav_numbers['nina']}")
# print(f"Cristiano favorite number is {fav_numbers['cristiano']}")
for name, numbers in fav_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"{number}")
