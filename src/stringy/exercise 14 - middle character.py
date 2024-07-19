# vstup z klavesnice bude random string a nasledne v nom vypisat stredne pismeno
from Functions.MathOperation import is_pair


def find_middle_char(string):
    length = len(string)
    if not is_pair(length):
        middle_index = length // 2
        middle_index2 = middle_index
    else:
        middle_index = (length // 2) - 1
        middle_index2 = length // 2
    return middle_index, middle_index2


user_string = input("Zadaj retazec: ")
middle1, middle2 = find_middle_char(user_string)
if not is_pair(len(user_string)):
    print(f"Stredne pismeno je: {user_string[middle1]}")
else:
    print(f"Stredne pismena su: '{user_string[middle1]}', '{user_string[middle2]}'")

