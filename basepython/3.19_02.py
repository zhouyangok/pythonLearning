#list
'''
classmates = ['12','34','56','78']
print(classmates)
print(classmates[0])
classmates.append(34)
print(classmates)
print(classmates[-3:])
print(classmates[0:3])
classmates.insert(2,'insert')
print(classmates)
print(classmates[2:9])
classmates.pop(1)
print(classmates[1])
print(len(classmates))
classmates.insert(2,['12','hello',45])
print(classmates)
'''

#tuple 不能修改的list
schoolmates = ('Michael','Bob','Tracy')
print(len(schoolmates))
print(schoolmates[1])
#捕获异常
try:
    schoolmates.pop(1)
except AttributeError as e:
    pass

for mate in schoolmates:
    print(mate)

a = list(range(5))
#print(a)
sum = 0
for b in list(range(101)):
    sum = sum+b
print(sum)

sun = 0
n = 99
while  n>0 :
    sun = sun+n
    n = n-2
print(sun)

tuple_01 = (1,2,3)
sum_01 = 0
for t in tuple_01:
    sum_01 = sum_01+t
print(sum_01)
