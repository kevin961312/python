#Ejercicios for and listas

numeros_veinte = list(range(1,21))
numeros_millon = list(range(1,10**6))
numeros_multi_tres = [numero*3 for numero in range(1,11)]
print(max(numeros_millon))
print(min(numeros_millon))
print(sum(numeros_millon))
print(numeros_veinte)
print(numeros_multi_tres)
cubos = []
for cubo in range(1,11):
    cubos.append(cubo**3)
    
print(cubos)

cubos_comprension = [cubo**3 for cubo  in range(1,11)]
print(cubos_comprension)