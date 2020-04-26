barra_separar = "\n#----------------------------------------------------------------------\n"
#Ejercicio 5-8, 5-9
#Usuarios
users = ['kevin','omar','admi','oscar','brayan','cata','lau']
#users = []
#Prueba if, si hay usuarios en la lista.
if users:
    print("\n\tThere are some users connected.\n")
else:
    print ("\n\tWe need to find some users connected!\n")
#Mensaje de ingreso.
for user in users:
    if user.lower() =='admi':
        print("\n\tHello "+user.title()+" would you like to see a status report?\n")
    else:
        print("\n\tHello "+user.title()+" thank you for loging in again.\n")
print(barra_separar)

#Ejercicio 5.10
occurent_users = ['kevin','omar','admi','oscar','brayan','cata','lau','ilda']
new_users = ['nicolas','jesus','maria','IlDa','kevin','omar']

for user_new in new_users:
    if user_new.lower() in occurent_users:
        print("\t\n"+user_new+" The username is not available.\n")
    else:
        print("\t\n"+user_new+" The username is available.\n")
print(barra_separar)

#Ejercicio 5.11
ordinals = [value for value in range(1,10)]
for ordinal in ordinals:
    if ordinal == 1:
        print (str(ordinal)+"st.")
    elif ordinal == 2:
        print (str(ordinal)+"nd.")
    elif ordinal == 3:
        print (str(ordinal)+"rd.")
    else:
        print (str(ordinal)+"th.")
        














