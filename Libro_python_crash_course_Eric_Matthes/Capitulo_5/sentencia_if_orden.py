barra_separar = "\n#----------------------------------------------------------------------\n"
#Variables
aliens = ['Green','Red','Blue','Yellow']
alien = 'YeLLow'
#Sentencia If alien
if alien.lower() == 'green':
    print("You earned 5 point. Congartulation!")
elif alien.lower() == 'red':
    print("You earned 10 point. Congartulation!")
elif alien.lower() == 'blue':
    print("You earned 15 point. Congartulation!")
elif alien.lower() == 'yellow':
    print("You win game. Congartulation!")
print(barra_separar)
#Sentencia if niñita :v
edad_persona = 80

if edad_persona < 2:
    print("\tThe person is a Baby and he have: "+str(edad_persona))
elif edad_persona < 4:
    print("\tThe person is a Toddler and he have: "+str(edad_persona))
elif edad_persona < 13:
    print("\tThe person is a Kid and he have: "+str(edad_persona))
elif edad_persona < 20:
    print("\tThe person is a Teenager and he have: "+str(edad_persona))
elif edad_persona < 65:
    print("\tThe person is a Adult and he have: "+str(edad_persona))
elif edad_persona > 65:
    print("\tThe person is a Older and he have: "+str(edad_persona))

print(barra_separar)
#ejercicio anterior con un for y if

ages = ["Baby","Toddle","Kid","Teenage","Adult","Older"]
if ages:
    print("\tYou can know, if you can enter.\n")
else:
    print ("\tYou can't know, if you can enter.\n")

for age in ages:
    if age == "Kid":
        print("\tYou can't enter, because you are "+age+" .\n")
    else:
        print("\tYou can enter, because you are "+age+" .\n")




















