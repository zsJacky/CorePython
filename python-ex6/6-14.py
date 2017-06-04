#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def rochambeau(choice):
    gesture = ['stock', 'paper', 'scissor']
    winlist = [('stock', 'scissor'), ('paper', 'stock'), ('scissor', 'paper')]
    computer = random.choice(gesture)
    
    if choice not in gesture:
        return "please input again"
    
    if choice == computer:
        return "Tie"
    elif (choice, computer) in winlist:
        return "You Win"
    else:
        return "You Lose"
              
if __name__ == "__main__":
    choice = raw_input("please input a choice from stock, paper and scissor: ")
    print "you choose %s" % choice
    print rochambeau(choice)
    
    
    