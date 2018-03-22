'''
f = abs
a = f(-10)
print(a)
def add(x,y,f):
    return f(x)+f(y)
def f(x):
    return x*x
print(add(3,4,f))
'''

def f(x):
    return x*x

r = map(f,(range(1,12)))
print(list(r))

print(list(map(str,range(1,5))))