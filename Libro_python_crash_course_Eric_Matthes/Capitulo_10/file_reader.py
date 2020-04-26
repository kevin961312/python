filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print (line)
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


filedigitspi = 'pi_million_digits.txt'

with open(filedigitspi) as file_pi:
    lines = file_pi.readlines()
    
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")