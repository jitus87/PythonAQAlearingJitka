# define class "Dice" with method "roll()" which returns a tuple (list read-only) with 2 values
import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second   # like this interpreter will define the result as tuple


dice = Dice()
print(dice.roll())

