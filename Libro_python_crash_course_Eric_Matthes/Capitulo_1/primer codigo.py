#Mensaje de inicio.
message = "Hello world"
print(message)

#Uso del método ".title(), .upper(), l.ower()".
name = "adam lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#concatenación de variables string
primer_nombre="kevin"
primer_apellido="pineda"
nombre= primer_nombre+" "+primer_apellido
print(nombre)
print("Mi nombre es: "+nombre.title()+".")

#Tabulacion de una variable string mediante el comando "\t".
#Nueva linea para una variable mediante el comando "\n".
mensaje_tabulacion= "\tUlises de James Joyce."
print(mensaje_tabulacion)
mensaje_nueva_linea= "Ulises:\nJames\nJoyce."
print(mensaje_nueva_linea)
mensaje_NL_T= "Podemos describir que:\nUlises de \n\tJames \n\tJoyce."
print(mensaje_NL_T)


#Espacios en blanco
lenguaje_favorito= " python "
print(lenguaje_favorito.rstrip())
print(lenguaje_favorito.lstrip())
print(lenguaje_favorito.strip())

#Apostrofe
message= " I'm kevin"
print(message)