class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(Point): 
    def __init__(self, p1, p2):
        self.p1 = p1.x, p1.y
        self.p2 = p2.x, p2.y

    def get_area(self):
        return (self.p2[0] - self.p1[0]) * (self.p1[1] - self.p2[1])

    def get_perimeter(self):
        return 2 * ((self.p2[0] - self.p1[0]) + (self.p1[1] - self.p2[1]))
    
    def is_square(self):
        if self.p2[0] - self.p1[0] == self.p1[1] - self.p2[1]:
            return True
        else:
            return False


p1 = Point(1, 3)
p2 = Point(3, 1)
rec1 = Rectangle(p1, p2)
print(rec1.get_area())