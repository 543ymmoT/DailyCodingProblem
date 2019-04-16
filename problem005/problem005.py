"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    """
    returns:
        function: a function that has another function as argument
    """
    def pair(func):
        """
        returns:
            function: a function that has a and b as arguments
        """
        return func(a, b)
    return pair

def car(func):
    return func(lambda a, b: a)

def cdr(func):
    return func(lambda a, b: b)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
