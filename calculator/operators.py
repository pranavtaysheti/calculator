""" Operators module """

class Operator():
    """ Operator class """

    pass

class Addition(Operator):
    
    symbol = "+"
    precedence = 2
    on_operand = "left"

    def operate(self, left, right):
        return left + right

class Substraction(Operator):

    symbol = "-"
    precedence = 2
    on_operand = "left"

    def operate(self, left, right):
        return left - right

class Multiplication(Operator):

    symbol = "*"
    precedence = 1
    on_operand = "left"

    def operate(self, left, right):
        return left * right

class Division(Operator):

    symbol = "/"
    precedence = 1
    on_operand = "left"

    def operate(self, left, right):
        return left / right

operators = {
    "+": Addition,
    "-": Substraction,
    "*": Multiplication,
    "/": Division,
}