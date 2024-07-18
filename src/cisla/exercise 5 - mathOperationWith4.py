# vstup z klavesnice budu 4 cele cisla a dane cisla nasledne spocitas, odpocitas, vynasobis, vydelis (mozu byt aj rozne kombinacie, fantazii sa medze nekladu)

import random

def print_results(scitanie, odcitanie, nasobenie, delenie):
    print(f"Vysledok scitania je: {scitanie}")
    print(f"Vysledok odcitania je: {odcitanie}")
    print(f"Vysledok nasobenia je: {nasobenie}")
    try:
        print(f"Vysledok delenia je: {delenie}")
    except NameError:
        pass


try:
    n1 = int(input("Zadaj 1. cislo: "))
    n2 = int(input("Zadaj 2. cislo: "))
    n3 = int(input("Zadaj 3. cislo: "))
    n4 = int(input("Zadaj 4. cislo: "))
except ValueError:
    print("Aspon 1 hodnota nie je cislo, skus znova")
else:

    scitanie = n1 + n2 + n3 + n4
    odcitanie = n1 - n2 - n3 - n4
    nasobenie = n1 * n2 * n3 * n4
    try:
        delenie = n1 / n2 / n3 / n4
    except ZeroDivisionError:
        print(" Delenie nie je mozne, deli sa nulou!")
        delenie = 'XXX'

    print_results(scitanie, odcitanie, nasobenie, delenie)

    print('''
    ----   nahodne operacie   ----

    ''')


    cisla = [n1, n2, n3, n4]
    # vyberieme nahodny pocet z 1-4cisla
    pocetVybratychCisel = random.randint(1,4)
    print(f"pocet vybranych cisel je: {pocetVybratychCisel}")

    # vyberieme nahodne cisla v pocte, aky sme nahodne vybrali vyssie
    nn = random.sample(cisla, pocetVybratychCisel)
    print('')
    print(f"Vybrane čísla su: {nn}")
    print('')

    # nastavime operacie na prvu hodnoty z listu a tym osetrime ak vybrane cisla budu v pocte 1
    scitanie = nn[0]
    odcitanie = nn[0]
    nasobenie = nn[0]
    delenie = nn[0]

    # urobime matematicke operacie, osetrime delenie nulou
    for i in range(1, pocetVybratychCisel):
        scitanie += nn[i]
        odcitanie -= nn[i]
        nasobenie *= nn[i]
        try:
            delenie /= nn[i]
        except ZeroDivisionError:
            delenie = 'XXX'

    print_results(scitanie, odcitanie, nasobenie, delenie)











