L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
'''
for i in list(range(3)):
    print(L[i])
print(L[0:3])
'''

#列生成器
a = list(range(1,12))
print(a)

L = []
for x in list(range(1,11)):
    L.append(x*x)
print(L)
#no.1
a = [x*x for x in range(1,11)]
print(a)
#no.2
b = [x*x for x in range(1,11) if x%2 ==0]
print(b)