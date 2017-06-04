def Calculate(expression):
    #if not type(expression) is types.StringType:
        #print "expression type is wrong, please input a correct \
                #string arithmetic expression, like this'1+2' " 

    symbols = ['+', '-', '*', '/', '%', '**']
    sym = ""
    
    for s in symbols:
        if s in expression:
            sym = s
    
    if sym == '':
        print "expression wrong"
        
    print sym
    nums = expression.split(sym)
    print nums
    n1 = float(nums[0])
    n2 = float(nums[1])
    
    if sym == symbols[0]:
        print "%s = %f" % (expression, n1 + n2)
        
    if sym == symbols[1]:
        print "%s = %f" % (expression, n1 - n2)
    
    if sym == symbols[2]:
        print "%s = %f" % (expression, n1 * n2)
        
    if sym == symbols[3]:
        print "%s = %f" % (expression, n1 / n2)
        
    if sym == symbols[4]:
        print "%s = %f" % (expression, n1 % n2)
        
    if sym == symbols[5]:
        print "%s = %f" % (expression, n1 ** n2)

if __name__ == '__main__':
    expression = raw_input("please input an expression: ")
    Calculate(expression)