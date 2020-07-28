from collections import Counter

def letter_frequency(setence):
    return Counter(setence)

print(letter_frequency("hello, my friends. How are you?"))
print(letter_frequency("hello, my friends. How are you?").most_common())

responses = [
    "vanilla",
    'chocolate',
    'vainilla',
    'vainilla',
    'caramel',
    'strawberry',
    'vanilla'
]

print("The children voted for {} ice cream.".format
(Counter(responses).most_common(1)[0][0]))