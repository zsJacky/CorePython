#!/usr/bin/env python 
import keyword
import string

alphas = string.letters + '_'
nums = string.digits

print "welcome to the id checker V2.0"
print "testees must be at least 2 chars long."
inp = raw_input(">")

flag = True

if inp in keyword.kwlist:
    flag = False
    print "Invalid the identifier must not be keyword"
    
if len(inp) > 1:
    if inp[0] not in alphas:
        flag = False
        print "invalid: first symbol must be alphabeetic"
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphas + nums:
                flag = False
                print "invalid"
                break
    if flag == True:
        print "okay as an identifier"
