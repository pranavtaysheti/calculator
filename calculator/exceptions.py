""" This module contains exception classes to be used everywhere. """

class ExpressionError(Exception):
    """ Is raised when an invalid charecter is found in expression """

    pass

class InvalidTokenError(Exception):
    """ Is raised when an invalid token is detected """

    pass