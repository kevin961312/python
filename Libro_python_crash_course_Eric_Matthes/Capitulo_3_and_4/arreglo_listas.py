#Ordenacion de listas metodo .sort(), orden lexicografico
cars = ['bmw','audi','toyota','ferrari']
cars.sort()
print(cars)
#Orden antilexicografico
cars = ['bmw','audi','toyota','ferrari']
cars.sort(reverse=True)
print(cars)

#Uso de la función sorted() para ordenar pero mantener el orden original.
print("Nuestra lista original es: \n")
print(cars)
print("\n")
print("Nuestra lista original es: \n")
print(sorted(cars))
print("\n")

#Imprimir una orden reverso usando la función .reverse()
cars = ['bmw','audi','toyota','ferrari']
print(cars)
cars.reverse()
print(cars)
print("\n")

#Imprimir la longitud de una cadena
longitud = len(cars)
print(longitud)