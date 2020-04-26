#Funcion de nombre, apellido, segundo nomnbre
def get_optional_name(first_name,last_name, middle_name=''):
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    full_name = full_name.lower()
    return full_name.title()

#Inicio del codigo, en el cual se ingresan los valores, para mostrar los nombres
active = True
#Bucle while para obtener nombres
while active:
    print("\nPlease tell me your name: ")
    f_name = input("\n\tFirst name: \n\t")
    l_name = input("\n\tLast name: \n\t")
    #Bucle while para pedir el middle name
    true_middle = True
    while  true_middle:
        active_middle = input("\n\tYou wish enter the middle name (yes/no): ")
        if active_middle.lower() == 'yes':
            m_name = input("\n\tMiddle name: \n\t")
            formatted_named = get_optional_name(f_name, l_name,m_name)
            print("\n\tHello, "+ formatted_named+"!")
            true_middle = False
        elif active_middle.lower() == 'no':
            formatted_named = get_optional_name(f_name, l_name)
            print("\n\tHello, "+ formatted_named+"!")
            true_middle = False
        else:
            true_middle = True
    true_middle = True
    #Bucle while para apagar no ingresar más nombres
    while true_middle:
        quit_program = input("\n\tEnter other name (yes/no): ")
        if quit_program.lower() == 'yes':
            true_middle = False
        elif quit_program.lower() == 'no':
            true_middle = False
            active = False
        
        
        
        
        
        
        
        
        
        
        