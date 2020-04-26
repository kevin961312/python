barra_separar = "\n#----------------------------------------------------------------------\n"
#Ejercicio 6.4

glossary = {
    "append": "Añade elemento a una lista.",
    "range(a,b)": "Crea un rango de numeros de a hasta b-1.",
    "title()": "Coloca la primera letra de un string en mayuscula.",
    }

glossary['upper'] = "Permite colocar todos los caracteres de un string en mayuscula."
glossary['lower'] = "Permite colocar todos los caracteres de un string en minuscula."
for word, meaning in glossary.items():
    print("\n\t"+word.title()+": \n\t"+meaning.title())
    
 print(barra_separar)   
