barra_separar = "\n#----------------------------------------------------------------------\n"

#Uso de la función range.
for value in range(1,10):
    print(value)
    
print(barra_separar)

#Uso de la clase list().

numbers = list(range(1,11))
print(numbers)
print(barra_separar)

#Otro uso de la función range.
#range(a,b,c), toma el número inicial de la lista "a" y le suma "c", 
#es decir [a,a+c,a+2c,...].
even_numbers = list(range(2,11,2))
print(even_numbers)
odd_numbers = list (range(1,11,2))
print(odd_numbers)
print(barra_separar)

#Llenar una lista vacia.
cuadrados = []
for valor in range(1,11):
    cuadrados.append(valor**2)
print(cuadrados)
print(barra_separar)
#Uso de la funciones estadisticas.
digitos = list(range(1,11))
print(min(digitos))
print(max(digitos))
print(sum(digitos))
print(barra_separar)
#Listas por comprensión 
cuadrados_comprension = [valor**2 for valor in range(1,11)]
print(cuadrados_comprension)
print(barra_separar)








