def get_formatted_name(first_name, last_name):
    """Return full name"""
    full_name = first_name+' '+last_name
    return full_name.title()
    
musician = get_formatted_name('freddie', 'mercury'  )
print(musician)

#argument optional
def get_full_name(first_name, middle_name ,last_name):
    full_name = first_name+' '+middle_name+' '+last_name
    full_name = full_name.lower()
    return full_name.title()

musician = get_full_name('kevin','SeBastIaN','pineda')
print(musician)

def get_optional_name(first_name,last_name, middle_name=''):
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name+' '+last_name
    full_name = full_name.lower()
    return full_name.title()


famous = get_optional_name('kevin','pineda','sebastian')
print(famous)

#Returning a dictionary

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last': last_name}
    if age:
        person['age']= age
    return person

musician = build_person('Kevin','Pineda', 27)
print(musician)