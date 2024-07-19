# vytvoris pole o velkosti 10 prvkov, do ktoreho pomocou random funkcie vlozis cele cisla od 1 po 1000 a nasledne urcis ci dane cisla su parne alebo neparne;
# vytvoris pole o velkosti 10 prvkov, do ktoreho pomocou random funkcie vlozis cele cisla od 1 po 1000 a nasledne urcis ci dane su prvocisla alebo nie su prvocisla;

import random
from Functions.MathOperation import is_pair
from Functions.MathOperation import is_prime

randomList = []
even = []
odd = []
prime = []
notprime = []

for i in range(10):
    randomNum = random.randint(1,1000)
    randomList.append(randomNum)
    if is_pair(randomNum):
        even.append(randomNum)
    else:
        odd.append(randomNum)

    if is_prime(randomNum):
        prime.append(randomNum)
    else:
        notprime.append(randomNum)

print(randomList)
print(f"Parne cisla su: {even}")
print(f"Nearne cisla su: {odd}")
print(f"Procisla su: {odd}")
print(f"Neprvocisla su: {odd}")






