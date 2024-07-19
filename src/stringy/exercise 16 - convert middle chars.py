# vstup z klavesnice bude random string a nasledne v vymenit stredne pismena: Slovo = Svolo len 2 alebo 3 v strede
from Functions.MathOperation import is_pair
from Functions.MathOperation import find_middle_char


def vymen_stred(retazec):
    if len(retazec) == 1:

        print("Prilis kratky retazec!")
        swapped = retazec

    elif is_pair(len(retazec)):
        middle_index1, middle_index2 = find_middle_char(retazec)
        swapped = retazec[:middle_index1] + retazec[middle_index2] + retazec[middle_index1] + retazec[middle_index2+1:]
    else:
        middle_index1, middle_index2 = find_middle_char(retazec)
        swapped = (retazec[:middle_index1-1] + retazec[middle_index1 + 1] + retazec[middle_index1] +
                   retazec[middle_index1 - 1] + retazec[middle_index1 + 2:])


    return swapped


retazec = input("Zadaj slovo: ")
print(f"Slovo s vymenenym stredom je: {vymen_stred(retazec)} ")

