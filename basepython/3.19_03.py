#dict 字典
try:
    d = {"zhou":100,"li":99,"wang":100}
    print(d['zhou'])
    d['zhang'] = 80
    print(d['zhang'])
    d['zhang']=90
    print(d['zhang'])
    print(d['james'])
except KeyError as e:
    print('ok~')

s = {"zhou":100,"li":99,"wang":100}
for k in s:
    print(s.get(k))

#set 只存key，不存value，所以不能存重复值
st = set([1,2,3,2,3,4])
st.add(5)
print(st)
