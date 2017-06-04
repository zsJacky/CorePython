#!/usr/bin/env python
# -*- coding:utf-8 -*-

def key2value(dict):
    d = {}
    for k in dic.keys():
        d[dic[k]] = k
    
    return d
if __name__ == '__main__':
    dic = {1: 'abc', 2: 'def', 3: 'ghi'}
    print dic
    print key2value(dic)