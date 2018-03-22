#C:\Users\medo_zy\Desktop
#读文件
'''
try:
    f = open('C:/Users/medo_zy/Desktop/新建文本文档.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
'''

with open('C:/Users/medo_zy/Desktop/新建文本文档.txt','r') as f:
    print(f.read())

with open('C:/Users/medo_zy/Desktop/python.txt', 'w') as f:
        f.write("Hello,python")
        