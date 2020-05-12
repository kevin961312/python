def next_(n,x):
    return (x+n/x)/2
n = 2
f_1 = lambda x: next_(n,x)
a0 = 1.0
#sqrt_aprox = [round(x,4) for x in (a0, f(a0), f(f(a0)),f(f(f(a0))),)]
#print(sqrt_aprox)


def repeat(f,a):
    yield a
    for v in repeat(f,f(a)):
        yield v

print(repeat(f_1,a0))