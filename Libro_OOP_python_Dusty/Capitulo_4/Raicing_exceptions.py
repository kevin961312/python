import unittest

class TestFunction(object):
    def __init__ (self, M, func, solution):
        self.M = M
        self.func= func
        self.solution = solution

    def evaluation(self):
        f