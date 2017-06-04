#!/usr/bin/env python
# -*- coding:utf-8 -*-

def findchr(string, char):
    l = len(string)
    for i in range(l):
        if string[i] == char:
            return i

    return -1

def rfindchr(string, char):
    l = len(string)
    for i in range(-1, -l-1, -1):
        if string[i] == char:
            return i + l
        
    return -1

def subchr(string, origchar, newchar):
    str = ''
    for ochr in string:
        if ochr == origchar:
            ochr = newchar
        str += ochr    
    return str

def test():
    s1 = 'finish'
    s2 = 'i'
    s3 = 'c'
    print findchr(s1, s2)
    print rfindchr(s1, s2)
    print subchr(s1, s2, s3)
    
if __name__ == '__main__':
    test()

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    