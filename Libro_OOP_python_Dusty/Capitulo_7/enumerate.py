import sys 
filename = sys.argv[0]

with open(filename) as file:
    for index, line in enumerate(file):
        print('{0}: {1}'.format(index+1,line), end='')