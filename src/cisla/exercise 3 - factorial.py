# vstup z klavecnice bude cele cislo a pre dane cislo vypocitas faktorial

number = int(input("Zadaj cislo pre faktorial: "))

fact = 1
for i in range(2, number+1):  # aby aj 0 bol vysledok 1
    fact = fact*i
    i -= 1

print(f"vysledok {number}! je: {fact}")