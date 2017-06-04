#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''写单元测试'''
import unittest

def Integer2IP(num):
    "Integer to IP"
    
    num1 = int(num)
    IP = []
    for i in range(4):
        IP.append(str(num % 256))
        num /= 256
    return '.'.join(IP[::-1])

def IP2Integer(IP):
    "IP to Integer"
    
    Integer = 0
    node = []
    node = IP.split('.')
    
    for i in range(-1, -len(node)-1, -1):
        x = -(i+1)
        Integer += int(node[i]) * (256 ** x)
        
    return Integer

def test():
    "Just for test"
    # num = input("Enter an int number: ")
    print "The Integer to IP address is: ", Integer2IP(2555)
    print "IP Address to Integer is: ", IP2Integer(Integer2IP(2555))
    
if __name__ == '__main__':
    test()