#Recorrer un diccionario
user_0 = {
    'username': 'garfol',
    'first': 'kevin',
    'last': 'pineda',
    }
for key, value in user_0.items():
    print("\n\tKey: "+ key)
    print("\tValues: "+value)
    
#Recorrido for

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'c++',
    'kevin': 'python'
    }
for name, language in favorite_language.items():
    print("\n\t"+name.title()+ "'s favorite language is: "+language.title()+".")

#Recorrer los "keys" en un diccionario.
for name in favorite_language.keys():
    print("\n\t"+name.title())
    
#Se posee la misma respuesta si omitimos el  metodo .keys()
for name in favorite_language:
    print("\n\t"+name.title())
    
#Otro ejercicio con diccionarios.
friends = ['jen','edward']
for name in favorite_language.keys():
    print("\n\t"+name.title())
    if name in friends:
        print("\n\tHi "+name.title()+" , I see your favorite language is "+
              favorite_language[name].title()+"!")

#Verificar si una "key" posee un  "value"
if 'kevin' not in favorite_language.keys():
    print("\n\tKevin, please take our poll!")
else:
    print("\n\tKevin ,thank you for taking the poll!")

#Devolver los keys de un diccionario en orden.
for name in sorted(favorite_language.keys()):
    print("\n\t"+name.title()+ " ,thank you for taking the poll!")
    
#Devolver los valores sin la llave
print("\n\tThe following languages have been mentioned: ")
for language in favorite_language.values():
    print("\n\t"+language.title())
#Devolver los valores en orden.
print("\n\tThe following languages have been mentioned in orden: ")
for language in sorted(favorite_language.values()):
    print("\n\t"+language.title())

#Si existe algun lenguaje repetido podemos suprimirlo con el clase .set()
print("\n\tThe following languages have been mentioned in orden and without repetition: ")
    
for language in set(favorite_language.values()):
    print("\n\t"+language.title())
    




