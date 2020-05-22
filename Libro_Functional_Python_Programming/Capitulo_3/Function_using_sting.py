from decimal import Decimal
from decimal import InvalidOperation

def clean_decimal(text):
    if text is None: return text
    try:
        return Decimal(text.replace("$", "").replace(",", ""))    
    except InvalidOperation:
        return text

def replace(data, a, b):
    return data.replace(a,b)


replace = str.replace
print(replace("$12.45","$",""))

def remove(str, chars):
    if chars: return remove(str.replace(chars[0],""),chars[1:])
    return str
    