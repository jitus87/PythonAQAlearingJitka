# except of using the same method for 2 different classes, we use the method once and we let it inherit by other classes
# example:

# class Dog:
#    def walk(self):
#        print("walk")


# class Cat:
#    def walk(self):
#        print("walk")

# we create new class with the method "walk" and let other Animals to inherit it's method
class Mammal:
    def walk(self):      # this method will be inherited by Dog and Cat as well
        print("walk")


class Dog(Mammal):   # Dog inherits methods of Mammmal
    def bark(self):
        print("bark")    # method specific for Dog only


class Cat(Mammal):
    pass               # used to tell interpreteur that the class Cat will be empty


dog1 = Dog()
dog1.walk()
dog1.bark()

cat = Cat()
cat.walk()