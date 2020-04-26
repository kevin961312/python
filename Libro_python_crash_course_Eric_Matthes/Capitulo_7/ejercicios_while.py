#Ejercicios while

sandwinch_orders = ['peperoni', 'queso', 'bife', 'atun']
finished_sandwiches = []

while sandwinch_orders:
    current_sandwich = sandwinch_orders.pop()
    print("\n\tI made your "+current_sandwich.title()+" sadwinch.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print("\n\tThe "+sandwich+" sandwich finished." )    

word_even = 'Print every word in this sentence that has an even number of letters'
words = word_even.split()
for word in words:
    if len(word) % 2 == 0:
        print("\n\t"+word.title()+" is even.")
    else:
        print("\n\t"+word.title()+" is odd.")
        
#ejercicio 7-9
sandwinch_orders = ['peperoni', 'pastrami','queso', 'bife', 'atun', 'pastrami',
                    'criolla','pastrami']
print("\n\tExcuse me, we don't have pastrami.")
while 'pastrami' in sandwinch_orders:
    sandwinch_orders.remove('pastrami')
print("\n\tYou can choosee the following sandwiches: ")
for sandwich in sandwinch_orders:
    print("\n\t"+sandwich.title())

name_vacation = {}
other_name = True
while other_name:
    names = input("\n\tWhat is your name: \n\t")
    name_vacation[names] = input("\n\tIf you could visit one place in the world, "
                                    +"where would you go?\n\t")
    flag = True
    while flag:
        other_people = input("\n\tOther people wish enter our poll (yes/no): ")
        if other_people.lower() == 'yes':
            other_name = True
            flag = False
        elif other_people.lower() == 'no':
            other_name = False
            flag = False

for name, vacation in  name_vacation.items():
    print("\n\t"+name.title()+" would like visit "+vacation.title()+".")
            
            
            























        