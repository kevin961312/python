#Start with users that need to be confirmed,
# and a empty list to hold confirmed users
unconfirmed_users = ['kevin', 'laura', 'omar']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    
    print("Verifying user: "+current_users.title())
    confirmed_users.append(current_users)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
#Remover elementos de una lista corta
numbers = [1,2,3,1,2,5,6,8,4,9,1,1,1,1,1,1,3]
while int(1) in numbers:
    numbers.remove(1)
    
print(numbers)