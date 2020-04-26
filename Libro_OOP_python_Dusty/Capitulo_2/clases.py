import math

#La clase más básica en Python
class MyfirstClass:
    pass

#Crear un objeto llamandolo con la instancia de la clase.
a = MyfirstClass()
b = MyfirstClass()

#Añadir atributos a la clase básica.
class Point:
    'Represents a point in two-dimensional geometry coordinates'
    def __init__(self, coor_x=0, coor_y=0):
        '''Initialize the position of a new point. 
        the coordinates can be specified. If they are not the point defaults to the origins'''
        self.move(coor_x,coor_y)

    def move(self, coor_x, coor_y):
        ''' Move the point to a new location in 2D space'''
        self.coor_x = coor_x
        self.coor_y = coor_y
    
    def reset(self):
        'Reset the point back to the geometric origin: (0,0)'
        self.move(0,0)
    
    def calculate_distance(self, other_point):
       """Calculate the distance from this point to a second
        point passed as a parameter.
        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        return math.sqrt((self.coor_x - other_point.coor_x )**2+(self.coor_y - other_point.coor_y)**2)

point = Point(3,5)
print(point.coor_x, point.coor_y)
