global_adjustment=5
ifile =''
ofile =''
def some_function(a,b,t):
    global global_adjustment
    return a+b*t+global_adjustment

def open(iname, oname):
    global ifile, ofile
    ifile = open(iname,'r')
    ofile = open(oname,'w')

    
