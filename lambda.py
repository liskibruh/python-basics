# def multiply_by_2(given_list):
# 	result_list=[]
# 	for each_element in given_list:
# 		print(each_element*2)
		


#given_list = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0] 

# multiply_by_2(given_list)

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = list(map(lambda x:x**2, l))
# print(a)

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 =[]
for i in l : 
    a=lambda x:x**2
    l1.append(a(i))

print(l1)