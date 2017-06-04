#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
num = []
def fun(dirName):
    for i in os.listdir(dirName):
        if os.path.isdir(dirName + "\\" + i):
            fun(dirName + "\\" + i)
        else:
            num.append(dirName + "\\" + i)
fun(r"f:\Python\Lib")
hasDoc = False
strTemp = ""
fileobj1 = open("hasdoc.txt","a+")
fileobj2 = open("nodoc.txt","a+")
for i in num:
    fobj = open(i)
    for eachline in fobj:
        if (not hasDoc) and eachline.startswith('"""'):
            hasDoc = True
        elif hasDoc and eachline.startswith('"""'):
            hasDoc = False
            strTemp += eachline
            break
        if hasDoc:
            strTemp += eachline
        else:
            break
    if strTemp != "":
        fileobj1.write("filename: " + i + "\n")
        fileobj1.write("__doc__ is:" + "\n")
        fileobj1.write(strTemp + "\n")
    else:
        fileobj2.write("filename: " + i + "\n")
    strTemp = ""
    fobj.close()
fileobj1.close()
fileobj2.close()