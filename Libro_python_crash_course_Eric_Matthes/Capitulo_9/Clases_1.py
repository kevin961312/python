class Dog():
    """A simple attemp to model a dog."""
    def __init__(self,name, age):
        """Initialize name and age attribute."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title()+" is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!.")
        
        
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.roll_over()
my_dog.sit()

your_dog = Dog('lucy', 3)
print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()
your_dog.sit()


#Ejercicios primera sección clases
class  Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
       print("The name restaurant is "+self.restaurant_name.title()+
             " and cuisine type is "+ self.cuisine_type)
        
    def open_restaurant(self):
        print("The "+self.restaurant_name.title()+" is open.")
        
        
chinese_restaurant = Restaurant("chan chuen","china")
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()
        