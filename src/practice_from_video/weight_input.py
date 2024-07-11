weight = int(input("Weight "))

lb_or_kg = input("(L)bs or (K)g: ")
weight_name = lb_or_kg.lower()

if weight_name == "k":
    weight_changed = weight * 2.2
    mass = "pounds"
else:
    weight_changed = weight * 0.45
    mass = "kilograms"
print(f'You are {weight_changed} {mass}')





