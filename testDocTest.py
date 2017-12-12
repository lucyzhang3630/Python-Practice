# -*- coding: utf-8 -*-

def fact(n):
    '''
    a fact doc test
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

# code below run the doctest when this python file is called
# we could also run it by cmd command

if __name__ == '__main__':
    import doctest
    doctest.testmod()
