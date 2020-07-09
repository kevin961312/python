def countBits(n):
    num_bin = bin(n)
    cont = 0
    for num in str(num_bin):
        if num == '1':
            cont += 1
        else:
            pass
    return cont


print(countBits(4))