
try:
    num1 = int(input("Insert a number: "))
    num2 = int(input("Insert another number: "))
    
except ValueError:
    print("To add you need to pick a number!")

else:
    add = num1 + num2
    print(add)

