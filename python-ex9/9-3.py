#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fileLines(F):
    f = open(F, 'r')
    data = [line.strip() for line in f.readlines()]
    print len(data)
        
if __name__ == "__main__":
    F = raw_input("please enter a filename: ")
    fileLines(F)