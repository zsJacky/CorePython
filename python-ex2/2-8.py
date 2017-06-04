list = [1, 2, 3, 4, 5]
tuple = (1, 2, 3, 4, 5)

print sum(list)
print sum(tuple)

result = 0
for i in list:
    result += i
print result
    
i = 0
result = 0
while i < 5:
    result += list[i]
    i += 1
print result

input = raw_input("please input number: ")
result = 0
while input != 'exit':
    n = int(input)
    result += n
    input = raw_input("please input number: ")
print result
