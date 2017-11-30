def move(n, a, b, c):
    if n == 1:
        print('move from',a,'to',c)
    else:
        # move n-1 from a to b
        move(n-1,a,c,b)
        # move the biggest one from a to c
        print('move from',a,'to',c)
        # move n-1 from b to c
        move(n-1,b,a,c)


move(3, 'A', 'B', 'C')
