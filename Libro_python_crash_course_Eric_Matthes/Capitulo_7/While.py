current_number = input("Enter intenger number for generate a list of 1 to: ")
current_number = int(current_number)
list_number = 1
while list_number <= current_number:
    print(list_number)
    list_number += 1
    
#Dejar que un usuario decida cuando salir.
prompt = "\nTell me something, and I will repeat it back to you: "
prompt +=  "\nEnter 'quit' to end the progam. \n"
message = " "
while message.lower() != 'quit':
    message = input(prompt)
    message = message.lower()
    print(message.title())

#Implementación del flag en un while
active = True
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print(message)
        
#Uso del break para salir de un bucle.

prompt = "\nPlease enter the name of a city you have visited: "
prompt +=  "\nEnter 'quit' to end the progam. \n"

while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")
        
#uso del de break en el for

names = ['omar','oscar','kevin']

for name in names:
    if name.lower() == 'kevin':
        break 
    else:
        print(name.title())
    

