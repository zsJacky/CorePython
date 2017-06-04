#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

def isPrime(num):
    i = int(math.sqrt(num))
    
    while i > 1:
        if num % i == 0:
            return False
        i -= 1
    else:
        return True 

if __name__ == "__main__":
    print zip(range(20), (isPrime(num) for num in range(20)))