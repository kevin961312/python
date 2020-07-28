class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num


    def __lt__(self,object):
        if self.sort_num:
            return self.number < object.number
        return self.string < object.string

    def __repr__(self):
        return "{}:{}".format(self.string,self.number)

    def __eq__(self,object):
        return all((
            self.string == object.string,
            self.number == object.number,
            self.sort_num == object.number,
        ))

a = WeirdSortee('a', 4, True)
b = WeirdSortee('b', 3, True)
c = WeirdSortee('c', 2, True)
d = WeirdSortee('d', 1, True)
l= [a,b,c,d]
print(l)
l.sort()
print(l)
for i in l:
    i.sort_num = False

l.sort()
print(l)

l = ['hello',"HELP",'Helo']
l.sort()
print(l)
l.sort(key=str.lower)
print(l)

from operator import itemgetter
l= [('h',4),('n',6),('o',5),('p',1),('t',3),('y',2)]
l.sort(key=itemgetter(1))
print(l)    