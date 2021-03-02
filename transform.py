def f(a, b):
    return a**b

def transform(f):
    return lambda *args : f(*args[::-1])
    
g = transform(f)

print(g(4,5))