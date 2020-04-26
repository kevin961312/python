#Función contar números primos.
def count_prime(number):
    list_count = []
    for number in range(1,number+1):
        if number ==2  or number == 3:
            list_count.append(number)
        elif number % 2 == 0 or number % 3 == 0:
            pass
        if 2**number % number == 2 and 3**number % number == 3:
            list_count.append(number)
        else:
            pass
    return print(len(list_count))
count_prime(10000)

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return print(len(primes))



patternsn = {
    1:'  *  ',
    2:' * * ', 
    3:'*   *',
    4:'*****',
    5:'**** ',
    6:'   * ',
    7:' *   ',
    8:'*  * ',
    9:'*    ',
    }