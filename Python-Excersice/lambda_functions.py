x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(3, 2))


def myfunc(n):
    return lambda a: a * n
