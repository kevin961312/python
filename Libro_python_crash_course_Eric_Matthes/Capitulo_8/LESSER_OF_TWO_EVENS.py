#Definicion de la función menor o mayor dada una condición,
#Si los argumentos son pares la función imprime el menor,
#Si los argumentos son impares la función imprime al mayor.
def lesser_of_two_evens(first_number, second_number):
    if first_number % 2 ==0 and second_number % 2 ==0:
        if first_number < second_number:
            return print("\n\t"+str(first_number))
        elif second_number < first_number:
            return print("\n\t"+str(second_number))
        else:
            return print("\n\tThe numbers are equals!")
    elif first_number % 2 == 1 or second_number % 2 == 1:
        if first_number < second_number:
            return print("\n\t"+str(second_number))
        elif second_number < first_number:
            return print("\n\t"*first_number)
        else:
            return print("\n\tThe numbers are equals!")
    else:
        return print("\n\tThe numbers are equals!")
        
#Modelo para ingresar los valores.
#La funcion toma los valores less_of_two_events(a,b).
active = True
while active:
    number_a = input("\n\tEnter the first number: \n\t")
    number_b = input("\n\tEnter the second number: \n\t")
    lesser_of_two_evens(int(number_a), int(number_b))
    while True:
        yes_no = input("\n\tYou wish enter others numbers (yes/no): ")
        if yes_no.lower() == 'yes':
            break
        elif yes_no.lower() == 'no':
            active = False
            break
            
print("\n\tThanks you!")