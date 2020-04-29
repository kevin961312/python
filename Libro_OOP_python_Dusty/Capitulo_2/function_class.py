def format_string(string, formatter = None):
    '''Format a string using the formatterobject, which
    is excepted to have a format() method that accepts 
    a string'''
    class DefaultFormatter:
        '''Format a string in title case.'''
        def format(self,string):
            return str(string).title()
    if not formatter:
        formatter = DefaultFormatter()
        
    return formatter.format(string)


hello_string = "hello world, how are you today?"
print('\n\tInput: '+hello_string)
print('\n\tOutput:'+format_string(hello_string))