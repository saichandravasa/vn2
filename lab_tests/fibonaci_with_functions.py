# 1 find the length of the string
a = int(input('enter the number to find the fibonacci series : '))
def fibonacci_series(a):
    x = 0
    y = 1
    for i in range(a):
        c = x + y
        x = y
        y = c
        print(c,end=' ')
fibonacci_series(a)



