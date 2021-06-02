""" Contains the cli interface for calculator """

import calculator.expression as expression
import calculator.expression_tree as expression_tree

ENTRY = "Welcome to Calculator!"
TAKE_INPUT = "Enter the expression:"
OUTPUT = "Answer is:"

def run():
    
    print(ENTRY)
    inp = input(TAKE_INPUT)
    exp = expression.ExpressionObjectList(inp)
    exp.objectify()
    stack = expression_tree.Stack(exp.objects)
    stack.make()
    stack.tree.solve()
    print (OUTPUT + str(stack.tree.result))