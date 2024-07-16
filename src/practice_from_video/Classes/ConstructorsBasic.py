# Constructor is a function that  is called at the time of creating an object (constructs = creates na object)

class Point:
    def __init__(self,x,y):
        self.x = x  # reference to current object
        self.y = y


point = Point(10,20)
print(point.x)

