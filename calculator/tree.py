""" Contains base classes for creating 'ExpressionTree' """

from typing import Optional

class Node():
    """ Each node represents an operation """

    def __init__(self, data):
        """
        self.data can be either an operator or an integer.
        """

        self.data = data
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def __repr__(self):
        
        return self.data

    def add_child(self, node: "Node", side: str):
        
        side_dict = {
            "left": "left_child",
            "right": "right_child"
        }

        setattr(self, side_dict[side], node)

class Tree():
    """ Each tree represents compiled expression """

    def __init__(self):

        self.top: Optional[Node] = None