import csv
from collections import namedtuple

def  row_iter(source):
    return csv.reader(source, delimiter=",")

def head_split(row_iter):
    title = next(row_iter)
    assert len(title) == 1 and title[0] == 'Cuarteto de Anscombe'
    heading = next(row_iter)
    assert len(heading) == 4 and heading == ['I', 'II', 'III', 'IIII']
    columns = next(row_iter)
    assert len(columns) == 8 and columns == ['x', 'y', 'x', 'y', 'x', 'y', 'x', 'y']
    return row_iter

#complemento uso de la seccion list, tuple and sets.

Pair = namedtuple('Pair',('x','y'))
def series(num, row_iter):
    for row in row_iter:
        yield Pair(*row[num*2:num*2+2])


with open("Capitulo_3/CSV/Anscombe.csv") as source:
    data = list(head_split(row_iter(source)))




with open("Capitulo_3/CSV/Anscombe.csv") as source:
    data = tuple(head_split(row_iter(source)))
    sample_I = tuple(series(0,data))
    sample_II = tuple(series(1,data))
    sample_III = tuple(series(2,data))
    sample_IV = tuple(series(3,data))
    print(str(data[0])+'\n')
    print(str(data[1])+'\n')
    print(str(data[2])+'\n')
    print(str(data[3])+'\n')
    print(sample_I)
    
    for subset in sample_I,sample_II,sample_III,sample_IV:
        mean = sum(float(pair.y) for pair in subset )/len(sample_I)
        print (mean)
        


