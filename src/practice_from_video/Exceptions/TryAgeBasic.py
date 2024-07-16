# example of exceptions - catch the exceptions in a code
try:
    age = int(input("Your age: "))
    print(age)
    income = 2000
    risk = income/age
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid value!")