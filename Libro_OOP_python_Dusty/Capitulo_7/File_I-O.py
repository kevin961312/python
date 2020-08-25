contents = "Some file contents"
file = open("filename", "w")
file.write(contents)
file.close()

with open('filename') as file:
    for line in file:
        print(line, end='')

class StringJoiner(list):
    def __enter__(self):
        return self
    def __exit__(self, type, value, tb):
        self.result = "".join(self)

import random, string
with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))
print(joiner.result)