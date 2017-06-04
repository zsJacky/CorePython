#!/usr/bin/env python 

def substrip(str):
    for i in range(len(str)):
        if str[i] != '':
            str = str[i:]
            break
    
    for i in range(-1, -len(str)-1, -1):
        if str[i] != '':
            str = str[:i+1]
            break
        
    return str
       
if __name__ == '__main__':
    str = raw_input("please input a string:")
    print substrip(str)