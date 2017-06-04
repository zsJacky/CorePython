#!/usr/bin/env python

def change(num):
    num_i = int(num)
    list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
             'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
             'sixteen', 'seven', 'eighteen', 'nineteen']
    list2 = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty'
             'seventy', 'eighty', 'ninety']
    
    if num_i == 1000:
        return 'one thousand'
    if num_i == 0:
        return 'zero'
    if num_i >= 100 and num_i % 100 == 0:
        return list1[num_i / 100] + 'hundred'
    str = ''
    if num_i / 100 > 0:
        str += list1[num_i / 100] + ' hundred and '
        num_i %= 100
    if num_i % 10 == 0:
        str += list2[num_i / 10]
        return str
    elif num_i < 20:
        str += list1[num_i]
        return str
    else:
        str += list2[num_i / 10] + '-' + list1[num_i % 10]
        return str
    
if __name__ == '__main__':
    num = raw_input("please input a number: ")
    print change(num)

