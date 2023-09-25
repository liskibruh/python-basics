def product(first, *args):
	result = first
	for elem in args:
		result=result*elem
	return result

print(product(1,2,3,6))