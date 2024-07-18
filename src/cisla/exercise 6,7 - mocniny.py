# vstup z klavesnice bude cele cislo a pre dane cislo vypocitas druhu/tretiu/xtu mocninu (tiez vstup z klavesnice)

try:
    cislo = int(input("Zadaj cele cislo: "))
    mocnina = int(input("zadaj mocninu: "))
except ValueError:
    print("Toto nie je cislo!!")
else:
# built-in operation
    #vysledok1 = pow(cislo, mocnina)
# my solution
    if cislo == 0 & mocnina == 0:
        vysledok2 = 1
    else:
        vysledok2 = cislo
        if mocnina > 0:
            for i in range(1, mocnina):
                vysledok2 = vysledok2*cislo
                # vypiseme kazdu mocninu od 2 do zadanej
                print(f"Mocnina {i+1} z cisla {cislo} je: {vysledok2}")
        else:
            predvysledok = cislo
            for i in range(1, abs(mocnina)):
                predvysledok = predvysledok * cislo
            vysledok2 = 1/predvysledok
            print(f"Mocnina {i} z cisla {cislo} je: {vysledok2}")

    print(f"Vysledok je: {vysledok2}")