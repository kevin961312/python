alien_0 = {'color': 'yellow', 'point': 5}
alien_1 = {'color': 'blue', 'point': 10}
alien_2 = {'color': 'green', 'point': 15}
list_aliens = [alien_0,alien_1,alien_2]
for alien in list_aliens:
    print(alien)

#crear aliens
aliens = []

#Make 30 aliens yellow

for alien_number in range(30):
    new_aliens = {'color': 'yellow', 'point': 5, 'speed': 'slow'}
    aliens.append(new_aliens)
    
#Show the first 5 alien
for alien in aliens[:5]:
    print(alien)
print("...")

print("Number of aliens yellos are: "+str(len(aliens)))

#Modificar elementos de un lista de diccionarios
for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien ['color'] = 'green'
        alien ['point'] = 10
        alien ['speed'] = 'medium'
        
for alien in aliens[:5]:
    print(alien)
    