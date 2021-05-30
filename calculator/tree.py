""" Contains base classes for creating 'ExpressionTree' """

from typing import Optional

class Node():
    """ Each node represents an operation """

    def __init__(self, data):
        """
        self.data can be either an operator or an integer.
        """

        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def add_child(self, parent: "Node", side: str):
        
        side_dict = {
            "left": self.left,
            "right": self.right
        }

        side_dict[side] = self

class Tree():
    """ Each tree represents compiled expression """

    def __init__(self):

        self.top: Optional[Node] = None