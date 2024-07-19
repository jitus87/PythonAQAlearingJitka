# vstup z klavesnice bude random string a nasledne v nom zamenit poradie pismen - reverzne

def reverse_text(retazec):
    return retazec[::-1]


retazec = input("Zadaj retazec ")
reverse = reverse_text(retazec)
print(f"Reverzny retazec je: {reverse}")
