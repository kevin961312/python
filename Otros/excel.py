#Libreria para caracteres.
import string
#Libreria para funciones Matematicas.
import math
#variables 
columna_ingresar = 16383
letras= list(string.ascii_uppercase)
modulo_letra= columna_ingresar%26
piso_decenas= math.floor(columna_ingresar/26)-1 
modulo_centenas= piso_decenas%26
piso_centenas= math.floor(piso_decenas/26)-1

#Sentencia If 
if 0<=columna_ingresar<=25:
    print(letras[modulo_letra])    
elif (26<=columna_ingresar<=701):
    
    print(letras[piso_decenas]+letras[modulo_letra])
elif (columna_ingresar>702):
   
    print(letras[piso_centenas]+letras[modulo_centenas]+letras[modulo_letra])