def Convert():
    money = int(raw_input("please input a number that less than 100: "))
    use_table = {1: 0, 5: 0, 10: 0, 25: 0}
    keys = use_table.keys()
    keys.sort(reverse = True)
    
    tmp = money
    for key in keys:
        while tmp >= key:
            tmp -= key
            use_table[key] += 1
        if tmp < 1:
            break
    return use_table
        
    """"n = 0
    for key in use_table:
        n += use_table[key]
    return n"""
    
print Convert()
    

