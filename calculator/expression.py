""" Raw Expression Module """

from calculator.expression_tree import ExpressionTree
import calculator.operators as operators

class ExpressionError(Exception):
    """ Is raised when an invalid charecter is found in expression """

    pass

class ExpressionObjectList():
    """ Contains list of expression objects. """

    def __init__(self, expression: str):

        self.expression_str = expression
        self.objects = []
        self.curr = []
        self.isoperatorallowed = False

    def objectify(self):
        """ Converts the expression string in objects in series.
        Each object is either a number or an operator
        """

        for char in self.expression_str:
            self.evaluate_char(char)

    def flush(self):
        
        number = 0
        
        for digit in self.curr:
            number = number*10 + int(digit)
        
        self.objects.append(number)
        self.isoperatorallowed = True

    def evaluate_char(self, char: str):
        """ Evaluates character and adds apporpriate object accordingly """
        
        if not char.isdecimal and char in operators.operators:

            if self.isoperatorallowed:
                self.flush()
                self.objects.append(operators.operators[char])

            else:
                raise ExpressionError

        elif char.isdecimal:
            self.curr.append(char)

        else:
            raise ExpressionError