# -*- coding: utf-8 -*-

import base64

#the default decode of base64 will remove "=" in the string,
#below function is for decoding using the string with "=="
#The b denotes a byte string.

def safe_base64_decode(s):
    remainder = len(s)%4
    if remainder != 0:
        return base64.b64decode(s + b'='*(4-remainder))
    else:
        return base64.b64decode(s)

# TEST:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')


# a better formal solution
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    return base64.b64decode(completing(s))

def completing(s):
    '''
    Function to completing a binary string with '='

    Example:

    >>> print(completing(b'a'))
    b'a==='
    >>> print(completing(b'ab'))
    b'ab=='
    >>> print(completing(b'abc'))
    b'abc='
    >>> print(completing(b'abcd'))
    b'abcd'
    '''
    slen = len(s)
    if slen == 0:
        return s
    num = slen % 4
    return s + b'=' * (4 - num) if num > 0 else s

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# TEST:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
