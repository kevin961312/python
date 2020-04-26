current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
stop_x = 1
while stop_x <= 5:
    print(stop_x)
    stop_x += 1
    
#no_stop_x = 1
#while no_stop_x <= 5:
#    print(no_stop_x)
    
cost = "\nPlease enter your age for know the cost of ticket: \n"
message = ''
while message.lower() != 'quit':
    message = input(cost)
    message = int(message)
    if message <= 3:
        print("The ticket cost: $0")
    elif message <= 12:
        print("The ticket cost: $10")
    elif message > 12:
        print("The ticket cost: $15")
    message = input("\nEnter 'quit' to end the program. \n")
    if message.lower() == 'quit':
        break
    else:
        print("You are going to continue.")
    
    