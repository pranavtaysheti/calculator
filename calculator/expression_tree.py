""" Expression Tree Module """

import calculator.operators as operators
import calculator.tree as tree
import calculator.exceptions as exceptions

from typing import Union
from typing import Type

class Number(tree.Node):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def solve(self):

        self.result = self.data
        return self.result
        
class Operation(tree.Node):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    def operate(self):

        self.result = self.data.operate(
            self.left_child.result,
            self.right_child.result)

    def solve(self): #BrainFuck
        """ Solves recursively """

        for node in self.right_child, self.left_child:
            node.solve()
        
        self.operate()

class ExpressionTree(tree.Tree):
    """ Represents expression in tree form """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    def solve(self):
        """ Solves the expression """

        self.top.solve()
        self.result = self.top.result

class Stack():
    """ Temporary stack used when building expression tree """

    def __init__(self, objects:list[Union[int, operators.Operator]]):
        self.operator_stack:list[Type[operators.Operator]] = []
        self.number_stack: list[int] = []
        self.operator_stack_precedence = 10
        self.objects = objects
        self.tree = ExpressionTree()
    
    def _pop_operator(self) -> operators.Operator:
        """ 
        Pops operator from 'operator_stack' and sets value of 
        'operator_stack_precedence' accordingly.
        """

        operator = self.operator_stack.pop()

        try:
            self.operator_stack_precedence = self.operator_stack[-1].precedence
        
        except:
            self.operator_stack_precedence = 10

        return operator

    def _final_flush(self):
        """ Used to flush the operator stack final time """

        while len(self.operator_stack):
            self._flush_operator()

    def _flush_stack(self, object: operators.Operator):
        """ Flushes all operators and puts number in right places """

        while object.precedence >= self.operator_stack_precedence: 
            self._flush_operator()

    def _flush_operator(self):

        operator = self._pop_operator()
        node = Operation(operator)
        node.add_child(self.number_stack.pop(), "right")
        node.add_child(self.number_stack.pop(), "left")
        self.number_stack.append(node)

    def _append_operator(self, operator: Type[operators.Operator]):

        self.operator_stack.append(operator)
        self.operator_stack_precedence = operator.precedence

    def make(self):
        """ puts the object in right order in result stack """

        for object in self.objects:

            if type(object) == int:
                number = Number(object)
                self.number_stack.append(number)

            elif issubclass(type(object), operators.Operator):

                if object.precedence < self.operator_stack_precedence:
                    self._append_operator(object)

                elif object.precedence >= self.operator_stack_precedence:
                    self._flush_stack(object)
                    self._append_operator(object)
        
        self._final_flush()

        self.tree.top = self.number_stack.pop()