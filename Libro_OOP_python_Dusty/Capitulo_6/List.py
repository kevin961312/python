import string
Characters = list(string.ascii_letters)+[" "]

def letter_frequency(sentence):
    frequencies = [(c,0) for c in Characters]
    for letter in sentence:
        index = Characters.index(letter)
        frequencies[index] = (letter, frequencies[index][1]+1)
    return frequencies
print(letter_frequency("hello my friends How are you"))