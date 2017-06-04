def hourTomin(a, b):
    return int(a) * 60 + int(b)

time = raw_input("please input the time format like this, HH:MM...:")
t = time.split(':')

print hourTomin(t[0], t[1])
