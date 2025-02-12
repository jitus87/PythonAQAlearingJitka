import random
import string

# Generation of random string
def generate_random_string(length):
    # Použijeme písmená
    characters = string.ascii_letters  # Malé a veľké písmená
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def random_year():
    return random.randint(2000,2024)     # random int 2000-2024

def random_price():
    return random.uniform(900, 2500)  # random cislo float 900-2500

def random_CPU():
    return random.choice(['Intel Core i9-13900K', 'AMD Ryzen 9 7950X', 'Apple M2 Max', 'Intel Xeon W9-3495X', 'AMD EPYC 9654'])  #pole: vyber model z pola

def random_HD_size():
    return random.choice(['256 GB', '512GB', '1TB', '2TB', '5TB'])  # pole: vyber z pola