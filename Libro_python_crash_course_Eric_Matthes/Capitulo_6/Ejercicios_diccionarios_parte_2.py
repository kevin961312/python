#Ejercicios pagina 6.7
barra_separar = "\n#----------------------------------------------------------------------\n"

user_peoples = {
    'garfol': {
        'first_name': 'kevin',
        'last_name': 'pineda',
        'age': 23,
        'city': 'bogota'
        },
    'rixuren': {
        'first_name': 'omar',
        'last_name': 'lopez',
        'age': 21,
        'city': 'bogota'
        },
    'eris': {
        'first_name': 'laura',
        'last_name': 'hernandez',
        'age': 100,
        'city': 'grecia'
        },
    }

for username, user_info in user_peoples.items():
    print("\nUsername: "+username)
    name = user_info['first_name']+" "+user_info['last_name']
    age  = user_info['age']
    city = user_info['city']
    print("\tFull name: "+name.title())
    print("\tAge: "+str(age))
    print("\tCity: "+city.title())

print(barra_separar)
    
#Ejercicio 6.8
perla = {
    'name': 'perla',
    'kind': 'cat',
    'owner': 'kevin pineda',
    }
sammy = {
    'name': 'sammy',
    'kind': 'dog',
    'owner': 'laura hernandez',
    }
mailo = {
    'name': 'mailo',
    'kind': 'dog',
    'owner': 'maria pineda',
    }

pets = [perla, sammy, mailo]

for pet in pets:
    print("\n\tFull name of pet is: "+pet['name'].title())
    print("\tKind of your pet is: "+pet['kind'].title())
    print("\tThe pet owner is: "+pet['owner'].title())

print(barra_separar)


#Ejercicio 6.9

favorite_place ={ 
    'omar': 'bogota',
    'kevin': 'medellin',
    'elena': 'cali',
    }
for name, city in favorite_place.items():
    print("\n\tThe favorite place of "+name.title()+" is: "+city)
    
print(barra_separar)

#Ejercicio 6.10

favorite_number = {
    'omar': 5,
    'kevin': 10,
    'elena': 15,
    'laura': 20,
    }
for name, number in favorite_number.items():
    print("\n\tThe number favorite of "+name.title()+" is "+str(number))
    
print(barra_separar)

#Ejercicio 6.11
cities = {
    'bogota': {
        'country': 'colombia',
        'population': 7000000,
        'fact': 'En Bogotá ocurrio el Bogotazo',
        },
    'lima': {
        'country': 'peru',
        'population': 9000000,
        'fact': 'Redescubrimiento de la ciudadela incaica Machu Pichu,'+
        'por el explorador estadounidense Hiram Bingham III.',
        },
    'quito':{
        'country': 'ecuador',
        'population': 1000000,
        'fact': "Primer grito de Independencia: 10 de agosto de 1809.",
        },       
    }

for city, city_info in cities.items():
    print("\nInformation about "+city.title()+": \n")
    print("\t"+city.title()+" is located in "+city_info['country'].title())
    print("\t"+city.title()+" has a population of : "+str(city_info['population'])
    print("\t"+city.title()+" happened the following: "+city_info['fact'])

print(barra_separar)












   