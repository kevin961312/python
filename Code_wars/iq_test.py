def iq_test(numbers):
    lista = list(numbers.split(" "))
    count_even = 0
    count_odd = 0
    for elem in lista:
        if int(elem) % 2 == 0:
            count_even += lista.index(elem)+1
        elif int(elem) % 2 == 1:
            count_odd += lista.index(elem)+1
    return min(count_odd,count_even)


print(iq_test("2 4 7 8 10"))
