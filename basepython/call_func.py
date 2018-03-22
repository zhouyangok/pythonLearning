# a = 100
# b = -100
# print(abs(a))
# print(abs(b))
# print(max(a,b))
#
# n1 =255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))
import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

a = -10
print(my_abs(a))

def fact(n):
    if n ==1:
        return 1
    return n*fact(n-1)

print(fact(1000))