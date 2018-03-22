#正则表达式
'''
[0-9a-zA-Z\_]+
[a-zA-Z\_][0-9a-zA-Z\_]*
[a-zA-Z\_][0-9a-zA-Z\_]{0,19}
^\d以数字开头
\d$以数字结尾
A|B可以匹配A或者B
'''

import re
def re_match(str):
    try:
        t = re.match(r'^\d{3}-\d{3,8}$',str)
        print(t)
    except TypeError as e:
        print(e)

re_match('123-2123')

test = 'a22'
if re.match(r'[a-zA-Z0-9][a-zA-Z0-9]\d$', test):
    print('ok')
else:
    print('failed')

strings = 'a b   c'
print(strings.split(' '))
print(re.split(r'\s+',strings))

#Email正则表达式
zhengze = '[0-9][a-zA-Z\_]@[a-z].com'
def validate_email(email):
    email_addr = re.compile(r'^[a-zA-Z\_]+.?[a-zA-Z]+@[a-zA-Z]+.com$')
    if email_addr.match(email) is None:
       print('failed')
    else:
        print('ok')

email_1 = 'someone@gmail.com'
email_2 = 'bill.gates@microsoft.com'
validate_email(email_1)