def factorial(n):
	if n == 1:
		return n
	return n * factorial(n-1)

if __name__ == '__main__':
	print factorial(6)