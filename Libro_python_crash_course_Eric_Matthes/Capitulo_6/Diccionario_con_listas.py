#Manejo de diccionarios que contienen listas.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print("\tYou ordered a "+pizza['crust']+"-crust pizza "+
      "with the following topping: ")
for topping in pizza['toppings']:
    print("\t"+topping+"\n")
    
#Ejemplos con la language

favorite_language = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python', 'haskell'],
    }
    
for name, languages in favorite_language.items():
    print("\n\t"+name.title()+ "'s favorite languages are: ")
    for language in languages:
        print("\t\t"+language.title())

        
