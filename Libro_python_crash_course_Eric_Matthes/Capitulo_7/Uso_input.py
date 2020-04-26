#Uso de la función input

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello "+name.title()+"!")

age = input("how old are you? ")
print("Your old is: "+age)
age = int(age)
print(age >= 15)

height = input("How tall are you, in meters: ")
height = int(height)
if height >=170:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    
#determinar si un numero es par o impar.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")    
    
#ejercicios input

car = input("what kind rental car do you like? ")
print("Let me see if I can find you a "+car.title()+".")

dinner_group = input("how many people are in their dinner group? ")
dinner_group = int(dinner_group)
if dinner_group > 8:
    print("They’ll have to wait for a table.")
else:
    print("Their table is ready.")

multiple_of_ten = input("Enter a number, and I'll tell you if it's multiple of ten: ")
multiple_of_ten = int(multiple_of_ten)
if multiple_of_ten % 10 == 0:
    print("\nThe number "+str(multiple_of_ten)+" is multiple of 10.")
else:
    print("\nThe number "+str(multiple_of_ten)+" is not multiple of 10.")    
    
