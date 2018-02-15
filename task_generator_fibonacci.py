
def fibonacci(f):
    a, b = 0, 1
    while f:
        a, b = b, a + b
        f -=1
        yield a

#for n in fibonacci(6):
#    print (n, end = " " )
