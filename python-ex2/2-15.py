a = raw_input("input a number: ")
b = raw_input("input a number: ")
c = raw_input("input a number: ")

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
        
print a, b, c

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
    
print a, b, c
