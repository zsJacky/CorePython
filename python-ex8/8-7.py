def getfactors(i):
    i = int(i)
    list = [i]
    num = i / 2
    while num >= 1:
        if i % num == 0:
            list.append(num)
        num -= 1
    
    return list

def isperfect(num):
	if sum(getfactors(num)) == 2*num:
		return 1
	else:
		return 0

if __name__ == '__main__':
	print isperfect(6)