#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def showTextbyPage(filename):
    f = open(filename, 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    n = 0
    for line in data:
        print line
        n += 1
        if n%25 == 0:
            os.system('pause')
            continue     
        
if __name__ == "__main__":
    filename = raw_input("please enter a filename: ")
    showTextbyPage(filename)