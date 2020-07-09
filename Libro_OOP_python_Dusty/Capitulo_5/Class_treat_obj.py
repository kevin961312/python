import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,point2):
        return math.sqrt((self.x-point2.x)**2+(self.y-point2.y)**2)

class Polygon:
    def __init__(self, points = None):
        points = points if points else []
        self.vertice = []
        for point in points:
            if isinstance(points,tuple):
                points = Point(*point)
            self.vertice.append(point)

    def add_point(self,point):
        self.vertice.append(point)
    
    def perimeter(self):
        perimeter = 0
        points = self.vertice + [self.vertice[0]]
        for ind in range(len(self.vertice)):
            perimeter += points[ind].distance(points[ind+1])
        return perimeter


square = Polygon((1,2))
square.add_point(Point(1,1))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
print(square.perimeter())