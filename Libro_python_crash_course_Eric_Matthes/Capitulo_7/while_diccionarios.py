responses = {}

#Set a flag for indicate that polling is active.

polling_active = True

while polling_active:
    #Promps for the person's name and response.
    name = input("\n\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #store response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    error = True
    while error:
        repeat =  input("Would you like to let another person respond? (yes/ no) ")
        if repeat.lower() == 'no':
            polling_active = False
            error = False
        elif repeat.lower() == 'yes':
            polling_active = True
            error = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

