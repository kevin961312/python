from collections import namedtuple

red = lambda color: color[0]
green = lambda color: color[1]
blue = lambda color:color[2]

Color = namedtuple("Color", ("red", "green", "blue", "name"))
print(Color.__contains__)
print(red('person'))
Person = namedtuple('Person', ('name', 'age', 'gender'))

name_tuple1 =Person('kevin',15,'masculino')
list_named = ['kevin',15,'masculino']
dict_named = {
    'name':'kevin',
    'age': 15,
    'gender':'masculino',
     }
print(name_tuple1.name)
print(name_tuple1.age)
print(name_tuple1.gender)
print(name_tuple1[0])
print(name_tuple1[1])
print(getattr(name_tuple1,'name'))



