#!/usr/bin/env python
# -*- coding:utf-8 -*-

def safe_open(filename):
    try:
        f = open(filename)
    except:
        f = None
    return f

if __name__ == "__main__":
    f = safe_open("file1.txt")
    print f