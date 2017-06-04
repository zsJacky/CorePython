# coding: utf-8
# 最大公约数用欧几里德算法求
# 两个数的乘积等于最小公倍数×最大公约数

def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a%b)

def lcm(a, b):
	return a * b / gcd(a, b)

if __name__ == '__main__':
	print gcd(15, 24)
	print lcm(15, 24)