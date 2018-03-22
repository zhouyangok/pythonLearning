# age = 20
# if age>18:
#     print('your age is',age)
#     print('adult')
# else:
#     print('your age is',age)
#     print('teenager')
#
# birth = input('birth')
# birth = int(birth)
# if birth<2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5
bmi = weight/(height*height)
print(bmi)
if bmi<=18.5:
    print("过轻")
elif bmi<=25 and bmi>18.5:
    print('normal')
elif bmi>25 and bmi<=32:
    print('too fat')
else:
    print('serious')