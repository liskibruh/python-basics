def linear_search(list, target):
	for i in range(len(list)):
		if list[i]==target:
			return i
	return None

def verify(index):
	if index is not None:
		print('Target found at index: ', index)
	else:
		print('Target not in the list')


numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,12)
verify(result)
result = linear_search(numbers, 5)
verify(result)