class Foo:
    @property
    def foo(self):
        return "bar"

#Decorator es equivalente a hacer foo = property(foo)

class Foo:
    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value


class Silly:
    @property
    def silly(self):
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        sel._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly
