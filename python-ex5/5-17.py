import random

ran_num = random.randint(1, 101)
list = range(ran_num)
for i in range(ran_num):
    list[i] = random.randint(-1, 2**31)
print ran_num
print list
list.sort
print list