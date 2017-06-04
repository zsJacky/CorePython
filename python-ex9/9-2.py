#!/usr/bin/env python
# -*- coding:utf-8 -*-

def displayFile(N, F):
    f = open(F, 'r')
    data = [line.strip() for line in f.readlines()]
    for line in data[:N]:
        print line
        
if __name__ == "__main__":
    N = input("please input a number to show how line will displayed: ")
    F = raw_input("please enter a filename: ")
    displayFile(N, F)