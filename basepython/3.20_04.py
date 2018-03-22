
edit_lsit = []
def greet_users(names):
    for name in names:
        msg = 'hello,'+ name.title()+'!'
        edit_lsit.append(msg)
    print(edit_lsit)
usernames = ['1','3','4']
greet_users(usernames)

#任意数量的实参
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)

make_pizza('peperoni')
make_pizza('peperoni','mushrooms',[1,2,3])

def make_rice(size,*others):
    print('make a '+str(size)+' something:')
    for topping in others:
        print(topping)

make_rice(12,'df','fda')

