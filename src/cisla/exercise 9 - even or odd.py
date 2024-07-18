# Vstup z klavecsnice je cele cislo, nasledne zistit ci dane cislo je parne alebo neparne (iny sposob ako %)

def is_pair(cislo):
    if cislo & 1:
        return False
    else:
        return True


try:
    cislo = int(input("Zadaj cele cislo: "))
except ValueError:
    print("Toto nie je cele cislo!!")
else:
    if is_pair(cislo) or cislo == 0:
        print(f"{cislo} je parne!")
    else:
        print(f"{cislo} je neparne!")
