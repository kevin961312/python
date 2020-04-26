def animal_crackers(text):
    list_string = text.split()
    if list_string[0].lower() == list_string[1].lower():
        return print(True)
    else:
        return print(False)
    
animal_crackers('la la')

def old_macdonald(name):
    list_caracters_name = [char for char in name]
    word = ''
    for caracter in list_caracters_name:
        if list_caracters_name.index(caracter) == 3 or list_caracters_name.index(caracter) == 0:
            word =  word + caracter.upper()
        else:
            word = word +caracter
    return print(word)

old_macdonald('macdonal')

def master_yoda_one(sentence):
    lis_carac_sentence = [char for char in sentence]
    word = ' '
    for caracter in range(len(lis_carac_sentence)):
        word = word + lis_carac_sentence[-caracter-1] 
    return print(word.strip())

master_yoda_one('I am home')

def master_yoda_two(sentence):
    lis_carac_sentence = sentence.split()
    word = ' '
    for caracter in range(len(lis_carac_sentence)):
        word = word+" "+ lis_carac_sentence[-caracter-1] 
    return print(word.strip())

master_yoda_two('I am home')


def almost_there(number):
    if abs(number-100) <=10:
        return print(True)
    elif abs(number-200) <=10:
        return print(True)
    else:
        return print(False)
    

def find_3_followed(list_numbers):
    for number in range(len(list_numbers)-1):
        if  list_numbers[number]==3 and list_numbers[number+1] == 3: 
            active = True
            break
        else:
            active = False
    return print(active)

find_3_followed([1,1,3,1,1,3,1,3,1,3,1,3,3])

def paper_doll(texts):
    word = ''
    for text in texts:
        word = word + text*3
    return print(word.strip())
paper_doll("hello")

def blackjack(num_1,num_2,num_3):
    if num_1+num_2+num_3 < 21:
        return print(num_1+num_2+num_3)
    elif ((num_1+num_2+num_3 > 21) and (num_1== 11 or num_2 == 11 or num_3 ==11) ):
        return print(num_1+num_2+num_3-10)
    else:
        return print("Bust")
blackjack(9,11,11)
blackjack(9,9,9)
blackjack(5,6,7)


def summer_69(arr):
    total = 0
    control = True
    for num in arr:
        while control:
            if num!=6:
                total += num
                break
            else:
                control = False
        while not control:
            if num !=9:
                break
            else:
                control = True
    return print(total)

summer_69([4, 5, 6, 7, 8, 9])
summer_69([1, 3, 5])
summer_69([2, 1, 6, 9, 11])

def spy_game(list_number):
    word = ''
    for number in list_number:
        if number == 0 or number == 7:
            word = word + str(number)
        else:
            pass
        if word == '007':
            break 
        else:
            pass
    if  word == '007':
        return print(True)
    else:
        return print(False)
    
    
spy_game([1,0,2,0,7,5,0,0,7])  




    
    

