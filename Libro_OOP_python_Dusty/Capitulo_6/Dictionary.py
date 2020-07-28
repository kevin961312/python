from collections import defaultdict
stock = {
    "GOOG": (613.30,625.86,610.50),
    "MSFT": (30.25,30.70,30.19)}
print(stock)
stock.get("RIM","Not Found")
stock.setdefault("BBRY",(10.50,10.62,10.39))
print(stock)
stock.setdefault("GOOG",(10.50,10.62,10.39))
print(stock)
for sto, values in stock.items():
    print("{} last values is {}".format(sto,values[0]))



random_keys = {}
random_keys['astring']= "somestring"
random_keys[5]= "anintenger"
random_keys[25.2]= "Float work too"
random_keys[("abc",123)]= "so do tuples"
print(random_keys)

class AnObject:
    def __init__(self, values):
        self.values = values

myobject = AnObject(14)
random_keys[myobject]= 'we van even store objects'
myobject.values = 12
try:
    random_keys[[1,2,3]]= "we can't store lists though"
except:
    print("unable to store list \n")

for keys, values in random_keys.items():
    print("{} has value {}".format(keys,values))
 #
#Defaultdict
def letter_frequency(setence):
    frequencies = {}
    for letter in setence:
        frequency = frequencies.setdefault(letter,0)
        frequencies[letter] = frequency + 1 
    return frequencies

print(letter_frequency("hello, my friends. How are you?"))


#Default dictionary 
def letter_frequency_t(setence):
    frequencies =  defaultdict(int)
    for letter in setence:
        frequencies[letter]+= 1
    return frequencies

print(letter_frequency_t("hello, my friends. How are you?"))

num_items = 0

def tuple_counter():
    global num_items
    num_items += 1 
    return (num_items, [])

default = defaultdict(tuple_counter)
default['a'][1].append("hello")
default['b'][1].append("world")
print(default)
