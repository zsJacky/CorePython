input = int(raw_input("please input a number between 1 and 100: "))
while input > 100 or input <= 1:
    input = int(raw_input("please input a number between 1 and 100: "))
print "your input number is:  %d" % input