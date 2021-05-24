""" Defining operator super-class """

class Operation():
    """Operator class

    An operator object contains following:
    Operator like "+", "-", "*", etc.
    Preceding number
    Succiding number
    """

    def __init__(self, symbol, left, right) -> None:

        self.left = left
        self.right = right
        self.result = None

""" Defining operators """

class Addition(Operation):
    
    symbol = "+"
    precedence = 2

    def operation(self, left, right):
        self.result = left + right

class Substraction(Operation):

    symbol = "-"
    precedence = 2

    def operation(self, left, right):
        self.result = left - right

class Multiplication(Operation):

    symbol = "*"
    precedence = 1

    def operation(self, left, right):
        self.result = left * right

class Division(Operation):

    symbol = "/"
    precedence = 1

    def division(self, left, right):
        self.result = left / right

operators = {
    "+": Addition,
    "-": Substraction,
    "*": Multiplication,
    "/": Division,
}