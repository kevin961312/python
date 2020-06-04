import random
some_exceptions = [ValueError, TypeError, IndexError, None]
try:
    choice = random.choice(some_exceptions)
    print("Raising: {}".format(choice))
    if choise:
        raise choise("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: {}".format(e.__class__.__name__))
else: 
    print("This code called if there is no exception")
finally:
     print("This cleanup code is always called")