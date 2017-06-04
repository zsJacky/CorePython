#!/usr/bin/env python 

num_str = raw_input('Enter a number: ')  
num_num = int(num_str) 
 

fac_list = range(1, num_num+1) 
print "BEFORE:", fac_list

i = 0 
fac_list2 = []
while i < len(fac_list):  
    if num_num % fac_list[i] != 0: 
        fac_list2.append(fac_list[i])
        #print fac_list2  
    i = i + 1

fac_list = fac_list2[:] 
 
print "AFTER:", fac_list