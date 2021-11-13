class Rectangle:
    def __init__(self, length,width):
        self.length = length;
        self.width = width;
    def area(self):
        return self.length*self.width

Rec1=Rectangle(6,7);
print("the area of the rectangle rec1 is",Rec1.area())