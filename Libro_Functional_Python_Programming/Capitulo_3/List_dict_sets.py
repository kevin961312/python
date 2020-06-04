print(range(10))
print([range(10)])
print([itera for itera in range(10)])
print(list(range(10)))
print([num for gen in [range(10), range(5)] for num in gen])

empty_list = []
for gen in [range(10),range(5)]:
    for num in gen:
        empty_list.append(num)

print(empty_list)
print(frozenset(range(10)))
    
