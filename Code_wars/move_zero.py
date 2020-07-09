def move_zeros(array):
    for ele in range(len(array)):
        if type(array[ele]).__name__== 'int' :
            array.append(array.pop(array.index(array[ele]))) 
    return array

print(move_zeros([0, 1, None, 2, 1, 0]))
print(type(False).__name__== 'int')