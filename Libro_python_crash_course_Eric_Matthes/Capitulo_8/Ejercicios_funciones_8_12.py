#Continuación funciones
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)


#Ejercicios sandwinch 8-12.
def order_sandwinch(list_orders):
    print("\nYou add to your sandwich: ")
    for order in range(len(list_orders)):
        print("\n\t"+str(order+1)+") "+list_orders[order].title()+".")

active = True
list_ingre = []
while active:
    ingre = input('\n\tWhat ingredient do you want in your sandwich?: \n\t')
    list_ingre.append(ingre)
    while True:
        quit_prog = input('\n\tDo you want another ingredient (yes/no): ')
        if quit_prog.lower() == 'yes':
            break
        elif quit_prog.lower() == 'no':
            active = False
            break

order_sandwinch(list_ingre)
    