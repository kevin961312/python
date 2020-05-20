class OddContainer:
    def __contains__(self,x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

from collections import Container
print(Container.__abstractmethods__)
#help(Container.__contains__)
Odd_Container = OddContainer()
print(isinstance(Odd_Container,Container))
print(issubclass(OddContainer,Container))
print(1 in Odd_Container)
print(2 in Odd_Container)



        