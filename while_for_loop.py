list_of_numbers = list(range(1,101))
final_list = []

for each_number in list_of_numbers:
	cube = each_number**3
	if cube%4==0 or cube%5==0:
		final_list.append(each_number)

print(final_list)