import math

square = [(1,1),(1,2),(2,2),(2,1)]

def distance(point_1, point_2):
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)

def perimeter(polygon):
    perimeter = 0
    points = polygon +[polygon[0]]
    for ind in range(len(polygon)):
        perimeter += distance(points[ind],points[ind+1]
    return perimeter


print(perimeter(square))