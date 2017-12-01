# treat each line as a list, use generator to output the list for next line
def triangles():
    rst = [1]
    while True:
        yield rst
        rst.append(0)
        rst = [rst[i-1]+rst[i] for i in range(len(rst))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
