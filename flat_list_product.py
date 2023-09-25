def product(input_list):
	flat_list = []
	for each_element in input_list:
		if type(each_element)==int or type(each_element)==float:
			flat_list.append(each_element)
		elif type(each_element)==list or type(each_element)==set or type(each_element)==tuple:
			#extract all the integers from the list, set or tuple
			#append them to flat_list

		#and so on..