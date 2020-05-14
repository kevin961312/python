numthree = 5
def example(numone, numtwo,a=5, **kw):
    global numthree
    return numone*numtwo*numthree

print(type(example))
print(example.__code__.co_varnames)
print(example.__code__.co_argcount)
print(example.__code__.co_freevars)
print(example.__code__.co_code)

merssene = lambda x: 2**x-1
print(merssene(17))
print(type(merssene))
print(merssene.__code__.co_varnames)
print(merssene.__code__.co_argcount)
print(merssene.__code__.co_freevars)
print(merssene.__code__.co_code)

year_cheese = [(2000,29.87),(2001,30.12),(2002, 30.6), (2003,30.66),
               (2004,31.33), (2005,32.62),(2006,32.73),(2007,33.5),
               (2008,32.84),(2010,32.92)]

print(max(year_cheese))
print(max(year_cheese, key =lambda yc: yc[1]))
print(max(map(lambda yc: (yc[1],yc),year_cheese)))

snd = lambda x: x[1]
print(snd(max(map(lambda yc: (yc[1],yc),year_cheese))))
