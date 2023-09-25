given_list = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0] 

def sort_list(given_list):

	#split to positive integers list and negative integers list
	positive_integers_list = []
	negative_integers_list = []

	for each_element in given_list:
		if each_element<0:
			negative_integers_list.append(each_element)
		elif each_element>=0:
			positive_integers_list.append(each_element)

	#sort both the lists one by one
	sorted_positive_integers_list = sorted(positive_integers_list)




	map(lambda given_list: give)