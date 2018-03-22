import random
card_list = [1,2,3,4]

n = 0
count = 0
total_count = 0
number = 10000000
while n<number:
    b = random.sample(card_list, 1)
    if b[0] == 1:
        count = 0
        total_count = total_count+1
    else:
        count=count+1
        if count == 4:
            count = 0
            total_count = total_count + 1
    n=n+1
print(total_count/number)