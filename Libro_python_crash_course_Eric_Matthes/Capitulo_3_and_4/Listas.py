bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0],bicycles[-1],bicycles[-2],bicycles[-3],bicycles[-4])
#Añadir un elemento a la lista, apartir del metodo .apped( )
bicycles.append('ducatti')
print(bicycles)
#Insertar un elemento en alguna posición de la lista, a partir del metodo .insert()
bicycles.insert(0,"ferrari")
print(bicycles)
#Eliminar elementos de una lista usando del
del bicycles[0]
print(bicycles)
#Remover algun elemento usando el metodo .pop( )
motocycles=[ 'honda','yamaha','suzuki']
print(motocycles)
popped_motocycles= motocycles.pop()
popped_site_especific = motocycles.pop(1)
print(motocycles)
print(popped_motocycles)
print(popped_site_especific)

#Remover algún elemento usando el metodo .remove()

motocycles=[ 'ducati','honda','yamaha','suzuki', 'ducati']

motocycles.remove('ducati')
print(motocycles)

