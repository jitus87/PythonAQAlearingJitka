# delenie cisiel a vysledok z delenia (+modulo): vstup z klavesnice cele cislo, nasledne zistit ci je dane cislo parne alebo neparne (pomocou %)

def is_pair(cislo):
    if cislo % 2 == 0:
        x = True
    else:
        x = False
    return x


try:
    cislo1 = int(input("Zadaj cele cislo 1: "))
    cislo2 = int(input("zadaj cislo 2: "))
except ValueError:
    print("Toto nie je cele cislo!!")
else:
    try:
        vysledok = cislo1 / cislo2
        modulo = cislo1 % cislo2
        print(f"Vysledok delenia {cislo1}/{cislo2} = {int(vysledok)} so zvyskom: {modulo}")
        cisla = [cislo1, cislo2]

        for i in range(2):
            if is_pair(cisla[i]):
                print(f"{cisla[i]} je parne")
            else:
                print(f"{cisla[i]} je neparne")

    except ZeroDivisionError:
        print(f"Delenie 0 nie je povolene!!!")
