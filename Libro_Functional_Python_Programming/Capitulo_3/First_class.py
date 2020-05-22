#Se observan funciones como objetos de primera clases es decir,
#podemos observar como se manejas las clases y sus herencias como
#como una funcion.

import collections

class Mersenne1(collections.Callable):
    def __init__(self,algorithm):
        self.pow_two = algorithm
    
    def __call__(self,arg):
        return self.pow_two(arg)-1

def shifty(number):
    return 1 << number

def multy(number):
    if number==0: return 1
    return 2*multy(number-1)
def faster(number):
    if number ==0: return 1
    if number%2 ==1: return 2*faster(number-1)
    t = faster(number//2)
    return t*t

m1s = Mersenne1(shifty)
m1m = Mersenne1(multy)
m1f = Mersenne1(faster)

print(len(str(m1f(11))),m1m(11),m1s(11))