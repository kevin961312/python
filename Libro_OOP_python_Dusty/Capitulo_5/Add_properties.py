class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def set_name(self,name):
        if not name:
            raise Exception("Invalid name")
        self._name = name
    
    def get_name(self):
        return self._name 

    name = property(get_name,set_name)

color = Color("#ff0000", "bright red")
print(color.get_name())
color.set_name("Red")
print(color.get_name())


#Más sencillo
class Color_two:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name
c = Color_two("#ff0000", "bright red")
c.name = "red"
print(c.name)
print(c.name)

class Color_three:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self,name):
        if not name:
            raise Exception("Invalid name")
        self._name = name
    
    def _get_name(self):
        return self._name 

    name = property(_get_name,_set_name)

c = Color_three("#ff0000", "bright red")
print(c.name)
c.name ="red"
print(c.name)
c.name = ""
print(c.name)