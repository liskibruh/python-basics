list_of_numbers = list(range(1,101))
final_list = []
i=0
while i<=100:
	cube = list_of_numbers[i]**3
	if cube%4==0 or cube%5==0:
		final_list.append(cube)
		i+=1
	print(final_list)