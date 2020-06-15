def compute_something(begin, end):
    global list_tuple
    crea_tuple = (begin,end)
    list_tuple.append(crea_tuple)

def legs(lat_lon_iter):
    begin= next(lat_lon_iter)
    for end in lat_lon_iter:
        yield begin, end
        begin= end
    
iterable =[1,2,3,5]
list_tuple = []
itera = iter(iterable)
begin = next(itera)
for end in itera:
    compute_something(begin,end)
    begin = end
print(list_tuple)
legs_test = list(legs(num for num in range(10)))
print(legs_test)
legs_test2 = list(legs( iter([0,1,2])))
print(legs_test2)