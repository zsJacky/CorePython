from __future__ import division

list = [1.3, 2.6, 3, 4.7, 5.3]

result = 0
for i in list:
    result += i
    avg = result / len(list)
print result
print avg
