import math

def isprimer(n):
    def isprime(k, coprime):
        if k < coprime*coprime:return True
        if k % coprime == 0:return False
        return isprime(k, coprime+2)
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime(n,3)

print(isprimer(52757))

def isprimeri(n):
    def isprimes(p):
        if p < 2: return False
        if p == 2: return True
        if p % 2 == 0: return False
        return not any(p == 0 for p in range(3,int(math.sqrt(n))+1,2))


