import time

@timer_test
def test():
	for i in range(5,100000):
		print(i)
		break

test2()