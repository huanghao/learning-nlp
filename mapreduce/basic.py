def double(i):
    return i * 2

def acc(a, b):
    return a + b

l = range(5)

print l
print map(double, l)
print reduce(acc, l, 0)


"""
map:
    input: k, v
    output: (k1, v1), (k2, v2), ...

reduce:
    input: k, (v1, v2, ...)
    output: k1, v1
"""
