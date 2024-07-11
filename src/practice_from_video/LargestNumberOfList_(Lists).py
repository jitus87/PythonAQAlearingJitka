# find the largest number in a list

list = [5,8,9,6,5,44]

largest = list[0]
for number in list:
    if number > largest:
        largest = number

print(f"Largest number is: {largest}")