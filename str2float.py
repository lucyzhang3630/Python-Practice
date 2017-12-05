from functools import reduce

def str2float(s):
    #first the integer part then the decimal part
    #turn the integer part of string to integer and the decimal part to integer first,
    # then turn the decimal part to decimal
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def num2rst(x,y):
        return x*10+y
    l = s.split('.')
    l[0] = reduce(num2rst,map(char2num,l[0]))
    l[1] = reduce(num2rst,map(char2num,l[1]))/(10**len(l[1]))
    return l[0]+l[1]


print('str2float(\'123.456\') =', str2float('123.456'))
