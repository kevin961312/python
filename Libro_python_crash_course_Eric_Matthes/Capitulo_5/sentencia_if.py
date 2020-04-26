#Sentencia if

cars = ['bmw','ferrari','honda','lamborgini','subaru']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

request_topping = "mushrooms"
if request_topping != "archive":
    print("Hold the anchovies!")

#Chequear si un elemento esta en una lista.

cars = ['bmw','ferrari','honda','lamborgini','subaru']

print('ferrari' in cars)
print('peperoni'in cars)

#Chequear que no esta en la lista.
cars = ['bmw','ferrari','honda','lamborgini','subaru']
car = 'Suzuki'

if car not in cars:
    print(car.title()+", no está en la lista.")
    