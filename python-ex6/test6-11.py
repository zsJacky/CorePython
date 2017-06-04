import nose
import chp6

def test_ip2integer():
	assert chp6.IP2Integer('0.0.9.251') == 2555

def teset_Integer2ip():
	assert chp6.Integer2IP(2555) == '0.0.9.251'

if __name__ == '__main__':
	nose.runmodule()