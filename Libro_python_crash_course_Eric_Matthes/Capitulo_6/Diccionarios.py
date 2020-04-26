#Diccionario
alien_0 = {'color':'green', 'point':5}
print( alien_0['color'] )  
print( alien_0['point'] )

new_point = alien_0['point']
print("\n\tYou just earned "+str(new_point)+" points!")

alien_0 ['x_position'] = 0
alien_0 ['y_position'] = 25

print(alien_0)

#Diccionario vacio
alien_1 = {}

alien_1['color'] = 'green'
alien_1['point'] = 5

print(alien_1)

#Modificar valores en un diccionario
alien_2 = {'color':'green', 'point':5}
print("The alien is color "+alien_2['color']+".")
alien_2['color'] = 'yellow'
print("Now, the alien is color "+alien_2['color']+".")

#Alien velocidad con diccionarios
alien_mov = {'x_position':0, 'y_position':25, 'speed':'fast', 'point':5}
print("Original x-position: "+str(alien_mov['x_position']))

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_mov['speed'].lower() == 'slow':
    x_increment = 1
elif alien_mov['speed'].lower() == 'medium':
    x_increment = 2
elif alien_mov['speed'].lower() == 'fast':
    x_increment = 3
else:
    x_increment = 0
    
alien_mov['x_position'] = alien_mov['x_position']+x_increment

print("New x-position: "+str(alien_mov['x_position']))

#Eliminacion valores de un diccionario.

print(alien_mov)

del alien_mov['point']

print(alien_mov)
    
    
    
    
    