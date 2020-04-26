filename =  'programming.txt'
active = True
with open(filename,'a') as file_object:
    while active:
        name = input("What is your name: ")
        print("Hello "+name+" thank you for to visited.")
        file_object.write(name.title()+" visited the page.\n")
        while True:
            following = input("if you want to continue write (yes/no):")
            if following.lower() == 'yes':
                break
            elif following.lower() == 'no':
                active = False
                break
                
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")