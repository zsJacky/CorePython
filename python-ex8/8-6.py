#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
# import pdb

def isprime(num):
    i = int(math.sqrt(num))
    
    while i > 1:
        if num % i == 0:
            return False
        i -= 1
    else:
        return True 

def getfactors(i):
    i = int(i)
    list = [i]
    num = i / 2
    while num >= 1:
        if i % num == 0:
            list.append(num)
        num -= 1
    
    return list

def getprimefactor(num):
    primefactor = []
    
    if isprime(num):
        primefactor.append(num)
        return primefactor
    else:
        # pdb.set_trace()
        factors = getfactors(num)
        factor = factors[-2]
        
        if isprime(factor):
            primefactor.append(factor)
            prime = getprimefactor(num / factor)
        elif isprime(num / factor):
            primefactor.append(num / factor)
            prime = getprimefactor(factor)
        else:
            prime = getprimefactor(factor)
            
        primefactor += prime 
        primefactor.sort()
        return primefactor
    
if __name__ == "__main__":
    print getprimefactor(20)

 
# def getprimefactor(n):
#     f = 2
#     while  f * f <= n:
#         while not n % f:
#             yield f
#             n //= f
#     f += 1
#     if n > 1:
#         yield n
    
# print max(getprimefactor(60085))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
