class SillyInt(int):
    def __add__(self, number):
        return 0

a = SillyInt(6)
b = SillyInt(5)
print(a+b)
print('-'*20)
print(dir(list))
print(len(dir(list)))
print('-'*20)
print(dir(set))
print(len(dir(set)))
print('-'*20)
print(dir(int))
print(len(dir(int)))

help(list.__add__)