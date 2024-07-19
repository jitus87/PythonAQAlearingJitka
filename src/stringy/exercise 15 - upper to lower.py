# vstup z klavesnice bude random string a nasledne v nom zamenit male pismena za velke a naopak

def convert_characters(string):
    new_string = ""
    for character in string:
        if character.islower():
            new_string += character.upper()
        elif character.isupper():
            new_string += character.lower()
        else:
            new_string += character
    return new_string


retazec = input("Zadaj retazec (velke/male pismena): ")
print(f"Cnverted string is: {convert_characters(retazec)}")
