def fib(n):
	i, a, b = 1, 0, 1
	while i < n:
		a, b = b, a+b
		i += 1
	return b

if __name__ == '__main__':
	print fib(6)