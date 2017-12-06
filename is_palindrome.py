import math
def is_palindrome(n):
    #palindrome means numbers like 12321, 909
    #this kind of number seems to be in odd digit
    #note: this method regard 0-9 as palindrome, if want to remove that, we could
    #add one more if condition
    obj = str(n)
    if len(obj)%2 != 0:
        for i in range(0,int(math.ceil((len(obj))/2))):
            if obj[i] != obj[len(obj)-1-i]:
                return
        return n


# a better solution
def is_palindrome1(n):
    n_str = str(n)
    #compares if n equals to the reverse of n, [::-1] means starting from the end to the beggining
    #counting down 1 each time, which means the reverse
    return n_str == n_str[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))
