#!/usr/bin/env python
# -*- coding:utf-8 -*-

def swap(str):
    str1 = ''
    for i in str:
        if i.isupper():
            str1 += i.lower()
        else:
            str1 += i.upper()
    return str1

if __name__ == '__main__':
    str = raw_input("please input a string: ")
    print swap(str)