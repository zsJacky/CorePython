#!/usr/bin/env python
# -*- coding:utf-8 -*-

def safe_input(inp):
    try:
        inputContent = raw_input(inp)
    except (EOFError, KeyboardInterrupt):
        inputContent = None
    return inputContent

if __name__ == "__main__":
    f = safe_input("input something: ")
    print f
        
