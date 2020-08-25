a = "Hello"
b = 'World'
c = ''' a multiple line string'''
d = """ More nmultiple"""
e = ("Three" "Strings" "Together")

print(float('45\u06602'))

s = a+b
print(s.count('l'))
print(s.find('l'))
print(s.rindex('l'))

s = 'hello world, how are you'
s2 = s.split()
s3 = s.partition(' ')
s4 = s.replace(' ', '**')
print(s2,s3,s4)