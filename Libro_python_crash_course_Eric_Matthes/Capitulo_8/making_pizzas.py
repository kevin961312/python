#importar un modulo y una funcion en especifico.
import pizza
from animal_carcker import old_macdonald
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
old_macdonald('macdonal')

#Import un modulo una funcion en esécifico y darle un alias
from animal_carcker import old_macdonald as mp

mp('macdonal')

#Importar un modulo y darle un alias
import animal_carcker as ac

ac.master_yoda_two('I am home')