def square(x):
	return x*x

def my_map(func,arg_list):
	result = []
	for each_elem in arg_list:
		result.append(func(each_elem))
	return result

arg_list = [1,2,3,4,5]

print(my_map(square, arg_list))