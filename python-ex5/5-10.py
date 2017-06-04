from __future__ import division

def convertC2F():
   f = int(raw_input("please input a Fahrenheit degree: "))
   c = (f -32) * (5 / 9)
   print "The related celsius degree is %f" % c

if __name__ == '__main__':
    convertC2F()