#!/usr/bin/env python
# -*- coding:utf-8 -*-

file1 = raw_input("Enter file1: ")
file2 = raw_input("Enter file2: ")

fp1 = open(file1)
fp2 = open(file2, 'a')
for line in fp1:
    fp2.write(line)
    
fp1.close()
fp2.close()