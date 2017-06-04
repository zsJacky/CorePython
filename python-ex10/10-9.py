#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math
import cmath

def safe_sqrt(num):
    try:
        ret = math.sqrt(num)
    except ValueError:
        ret = cmath.sqrt(num)
    return ret

if __name__ == '__main__':
    print safe_sqrt(12)
    print safe_sqrt(-1)
    