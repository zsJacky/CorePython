def Check(score):
    #score = raw_input("please input a score: ")
    if score >= 90 and score <= 100:
        print "A"
    elif score >= 80 and score <= 89:
        print "B"
    elif score >= 70 and score <= 79:
        print "C"
    elif score >= 60 and score <= 69:
        print "D"
    else:
        print "F"
        
Check(50)
        