from random import randint, choice


class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        result = randint(1, self.sides)
        print(result)


print("Dice one:")
dice_10 = Dice(10)
x = 0
while x < 10:
    dice_10.roll_dice()
    x += 1

print("Dice two:")
dice_20 = Dice(20)
x = 0
while x < 20:
    dice_20.roll_dice()
    x += 1
