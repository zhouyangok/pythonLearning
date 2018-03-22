def make_shirt(size,font_style):
    print('the T-shirt size is '+ size+",the font style is "+font_style)

make_shirt('L','宋体')

def build_person(first_name,last_name,middle_name =''):
    print('my name is '+ first_name+' '+ middle_name+' '+last_name)
build_person('li','he')

def build_dict_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_dict_person('jimi','hendrix',age = 27)
classcian = build_dict_person('lily','jimi')
print(musician)
print(classcian)