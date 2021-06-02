""" Raw Expression Module """

import calculator.exceptions as exceptions
import calculator.operators as operators

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
            self._evaluate_char(char)
        
        self._flush()

    def _flush(self):
        
        number = 0
        
        for digit in self.curr:
            number = number*10 + int(digit)
        
        self.objects.append(number)
        self.curr = []

    def _evaluate_char(self, char: str):
        """ Evaluates character and adds apporpriate object accordingly """
        
        if not char.isdecimal() and char in operators.operators:

            if self.isoperatorallowed:
                self._flush()
                self.objects.append(operators.operators[char]())
                self.isoperatorallowed = False

            else:
                raise exceptions.ExpressionError

        elif char.isdecimal():
            self.curr.append(char)
            self.isoperatorallowed = True

        else:
            raise exceptions.ExpressionError