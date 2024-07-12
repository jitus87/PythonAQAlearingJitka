def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome abroad")


print("Start")
greet_user("John", last_name="Smith")  #positional arguments are first, keyword arguments are second
greet_user("Mary", "Poppins")  # only positional arguments - order matters
greet_user(last_name="Doe", first_name="Jon")  #only keyword arguments - order doesn't matter
print("Finish")