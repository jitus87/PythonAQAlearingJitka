#remove duplicates from the list

list = ['Sarah','John','Bob', 'Sarah','Henry','Bob']
unique_list = []

duplicate = list[0]
for name in list:
    if name not in unique_list:
        unique_list.append(name)

print(unique_list)
