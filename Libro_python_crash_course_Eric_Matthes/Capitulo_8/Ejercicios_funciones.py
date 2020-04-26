#Ejercicio 8-6
def city_country(city, country):
    print(city.title()+", "+country.title())
city_country('bogota','colombia')


#Ejercicio 8-4
def make_album(artist_name, title_name):
    dicti_album = {
        'name': artist_name,
        'title': title_name,
        }
    print(dicti_album)

make_album('queen','a night it the opera')


def split_word(word):
    list_caract = [chara for chara in word]
    list_lo_up = []
    for char in list_caract:
        if list_caract.index(char) % 2 == 0:
            list_lo_up.append(char.lower())
        else:
            list_lo_up.append(char.upper())
    return print(''.join(list_lo_up))

split_word('kevin pineda')
        
def myfunc(string):
    new_string = ''    
    for i in range(len(string)):
        if (i+1) %2 == 0:
            new_string = new_string + string[i].upper()
        else:
            new_string = new_string + string[i].lower()
    return new_string
print(myfunc('Omar lopez'))
