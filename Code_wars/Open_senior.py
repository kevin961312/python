def openOrSenior(data):
    # Hmmm.. Where to start?
    lista_open = []
    for elemn in data:
        if elemn[0] >= 55 and elemn[1] > 7:
            lista_open.append("Senior")
        else:
            lista_open.append("Open")
    return lista_open

print(openOrSenior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))        