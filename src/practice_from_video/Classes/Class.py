# we use classes to define new types

class Point:
    def move(self):  #method of a class
        print("move")
    def draw(self):
        print("draw")


point1 = Point()  #class stored as an object. Object is instance of class Point
point1.x = 10  #attributes of a class anywhere in the program
point1.y = 20

print(point1.x)
point1.draw()