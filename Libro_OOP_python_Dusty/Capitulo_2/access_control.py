class SecretString():
    '''A not-all secure way to store a secret string'''
    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    
    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''

secret_string = SecretString("Acme: Top Secret","Jebus")
print(secret_string.decrypt("Jebus"))
