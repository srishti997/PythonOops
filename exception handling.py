class Error(Exception):
    def message(self):
        raise NotImplementedError()
class InputError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
    def message(self):
        print("Error in input in expression"),
        print(self.expr)
try:
    a = input("Enter a : ")
    raise InputError("input(\"Enter a : s\")", "Input Error")
except InputError as ie:
    ie.message()
