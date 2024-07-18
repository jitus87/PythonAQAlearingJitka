# vstup z klavesnice budu 2 cele cisla a dane cisla nasledne spocitas, odpocitas, vynasobis, vydelis

num1 = int(input("Zadaj 1. cislo: "))
num2 = int(input("Zadaj 2. cislo: "))

scitanie = num1 + num2
odcitanie = num1 - num2
nasobenie = num1 * num2
try:
  delenie = num1 / num2
except ZeroDivisionError:
    print("Delenie nulou nie je mozne! ")

print(f"Vysledok scitania je: {scitanie}")
print(f"Vysledok odcitania je: {odcitanie}")
print(f"Vysledok nasobenia je: {nasobenie}")
try:
    print(f"Vysledok delenia je: {delenie}")
except NameError:
    pass


