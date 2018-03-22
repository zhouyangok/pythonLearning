'''
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('lily',6)
my_dog.sit()
my_dog.roll_over()
'''

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("餐馆名称 "+ self.restaurant_name)
        print("餐馆类型 "+ self.cuisine_type)
    def open_restaurant(self):
        print('餐馆正在营业')

res = Restaurant("123",'df')
res.describe_restaurant()
res.open_restaurant()

