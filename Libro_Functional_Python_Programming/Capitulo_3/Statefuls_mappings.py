from collections import namedtuple

Color = namedtuple('Color',('red','green','blue','name'))

sequence = (
    Color(red=239, green=222, blue=205, name='Almond'),
    Color(red=205, green=149, blue=117, name='Antique Brass'), 
    Color(red=253, green=217, blue=181, name='Apricot'), 
    Color(red=197, green=227, blue=132, name='Yellow Green'), 
    Color(red=255, green=174, blue=66, name='Yellow Orange'))

name_map =  dict( (color.name, color) for color in sequence)

print(name_map)