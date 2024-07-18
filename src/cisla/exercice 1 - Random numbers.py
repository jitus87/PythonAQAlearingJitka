# Generovanie random cisla (integer, float), random textoveho retazca, random stringu(ktory bude obsahovat aj specialne znaky)

import random
import string

intNumber = random.randint(1,100)
print(f'Random integer is: {intNumber}')

floatNumber = random.random()
print(f"Random float is: {floatNumber}")

length = int(input("How many characters the string should have? "))
print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length)))


characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnoprqrstuvwxyz 123456789`~!@#$%^&*()_+=-][{};'|:/.,<>?|"
print(''.join(random.choices(characters, k=length)))




