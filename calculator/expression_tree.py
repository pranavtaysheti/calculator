""" Expression Tree Module """

import calculator.operators as operators
import calculator.tree as tree
import calculator.exceptions as exceptions

from typing import Union
from typing import Type
from typing import TYPE_CHECKING

class Operation(tree.Node):

    def operate(self):
        self.data.operate(self.left, self.right)

class ExpressionTree(tree.Tree):
    """ Represents expression in tree form """

    def solve(self):
        """ Solves the expression """

        pass

class Stack():
    """ Temporary stack used when building expression tree """

    def __init__(self, objects:list[Union(int, operators.Operator)]):
        self.operator_stack:list[Type(operators.Operator)] = []
        self.number_stack: list[int] = []
        self.operator_stack_precedence = None
        self.objects = objects
        self.isoperatorallowed: bool = True
        self.tree = ExpressionTree()
    
    def _pop_operator(self) -> operators.Operator:
        """ 
        Pops operator from 'operator_stack' and sets value of 
        'operator_stack_precedence' accordingly.
        """

        operator = self.operator_stack.pop()
        self.operator_stack_precedence = self.operator_stack[-1].precedence
        return operator

    def _final_flush(self):
        """ Used to flush the operator stack final time """

        try:
            while len(self.operator_stack):
                self._flush_operator

        except:
            print ("This is not supposed to happen in any case.")

    def _flush_stack(self, object: operators.Operator):
        """ Flushes all operators and puts number in right places """

        while self.operator_stack_precedence >= object.precedence: 
            self._flush_operator

    def _flush_operator(self):

        operator = self._pop_operator()
        node = tree.Node(operator)
        node.add_child(self.number_stack.pop(), "right")
        node.add_child(self.number_stack.pop(), "left")
        self.number_stack.append(node)

    def _append_operator(self, operator: Type(operators.Operator)):

        if self.isoperatorallowed:
            self.operator_stack.append(operator)
            self.operator_stack_precedence = operator.precedence

        else:
            raise exceptions.InvalidTokenError

    def make(self):
        """ puts the object in right order in result stack """

        for object in self.objects:

            if type(object) == int:
                self.number_stack.append(object)
                self.isoperatorallowed = True

            elif issubclass(type(object), operators.Operator):

                if object.precedence < self.operator_stack_precedence:
                    self._append_operator(object)

                elif object.precedence >= self.operator_stack_precedence:
                    self._flush_stack(object)
                    self._append_operator

                self.isoperatorallowed = False
        
        self._final_flush()

        self.tree.top = self.number_stack.pop()