def myrange(froms, to, increment):
	start = froms
	while start <= to:
		print start,
		start += increment

if __name__ == '__main__':
	myrange(2, 26, 4)