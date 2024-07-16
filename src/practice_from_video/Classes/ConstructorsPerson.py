# define Person with "name" attribute and "talk" method that print: hi I am : name attribute
# use the method talk for 2 different names

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")  # each object is an instance of a Person class
john.talk()

bob = Person("Bob Marley")  # each object is an instance of a Person class
bob.talk()