def numbers():
    for number in range(16):
        print('=',number)
        yield number

def sums_to(n):
    sums = 0
    for sum in numbers():
        if sum == n: break
        sums += sum
    return sums

print(sums_to(17))