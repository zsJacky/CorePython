#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fileFilter(filename):
    f = open(filename, 'r')
    allLines = f.readlines()
    f.close()
    for eachLine in allLines:
        index = eachLine.find("#")
        if index != -1:
            if index == 0:
                continue
            else:
                line = eachLine[0:index]
                print line
                continue
        print eachLine,
        
if __name__ == "__main__":
    filename = raw_input("Enter file name: ")
    fileFilter(filename)