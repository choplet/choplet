def fibonacci(f):
    a, b = 1, 1
    while f:
        a, b = b, a + b
        f -=1
        yield a

print(next(fibonacci(6)))
print(next(fibonacci(6)))
print(next(fibonacci(6)))
