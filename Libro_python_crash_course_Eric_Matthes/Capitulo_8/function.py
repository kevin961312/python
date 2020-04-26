#introducciona funciones
def greet_user(username):
    """Display a simple greeting."""
    print("Hello world. I'm "+username.title())
    
def display_message():
    """Message that i do"""
    print("I am learning about function in python. It's great!")
    


def favorite_book(name_book):
    """You can enter in the arggument, the title about your favorite boo<k"""
    print("Your favorite book is: "+name_book.title())
    
    
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a "+animal_type+".")
    print("\nMy "+animal_type+"'s name is "+pet_name.title()+".")
    
describe_pet('Cocker','Candy')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(pet_name, animal_type ='dog'):
    """Display information about a pet."""
    print("\nI have a "+animal_type+".")
    print("\nMy "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('jesus', 'cat')

#return values










