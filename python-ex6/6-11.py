def ip2int(ip):
	ip_list = ip.split(".")
	sum_int = 0
	for i in range(4):
		sum_int += int(ip_list[i]) * (256**(4-i-1))
	return sum_int

def int2ip(number):
	ip_list = []
	for i in range(4):
		ip_list.append(str(number/256**(4-i-1)))
		number %= 256 ** (4-i-1)
	return ".".join(ip_list)

if __name__ == "__main__":
	print ip2int("192.168.0.1")
	print int2ip(3232235521)
	print int2ip(ip2int("192.168.0.1"))