#函数调用
a = 100
b = -100
print(a==b)
print(a == abs(b))
c = '-100'
print(a == abs(int(c)))

#数据类型转换
a1 = int('123')
print(a1)
try:
    b1 = int('123.12')
    print(b1)
except ValueError as e:
    print(e)
b2 = '123.12'
print(float(b2))
b3 = 12.12
print(str(b3) == b3)

def func_demo(x):
    print(x*x)
func_demo(2)


#循环求值
def func_xn(x,n):
    s = 1
    while n>0:
        s = s*x
        n = n-1
    return s

print(func_xn(3,3))

#给函数默认值
def enroll(name,gender,age=10,city='shanghai'):
    data={
        'name':name,
        'gender':gender,
        'age':age,
        'city':city
    }
    return data

data1 = enroll('张无忌','男')
data2 = enroll("赵敏",'女',18,'金陵')
print(data1)
print(data2)

#递归
def func_degui(x):
    if x ==1:
        return 1
    else:
        return x*func_degui(x-1)

s = func_degui(3)
print(s)
