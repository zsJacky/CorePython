#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getfactors(i):
    i = int(i)
    list = [i]
    num = i / 2
    while num >= 1:
        if i % num == 0:
            list.append(num)
        num -= 1
    
    return list

if __name__ == "__main__":
    print getfactors(20)
    
    