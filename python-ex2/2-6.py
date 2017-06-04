def Intchk(num):
    if num > 0:
        print "the number you input is positive"
    elif num == 0:
        print "the number you input is zero"
    else:
        print "the number you input is negative"

num = 2
Intchk(num)

input = int(raw_input("please input a number:"))
while input != 'exit':
    Intchk(input)
    input = int(raw_input("please input a number:"))

        