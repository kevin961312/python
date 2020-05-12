class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling of method on Base Class")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling of method on Left Subclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling of method on Right Subclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass,RightSubclass):
    num_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_calls +=1


subclass_o = Subclass()
subclass_o.call_me()
print(
    subclass_o.num_calls,
    subclass_o.num_left_calls,
    subclass_o.num_right_calls,
    subclass_o.num_base_calls
)