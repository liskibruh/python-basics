def get_formatted_name(first_name, last_name, middle_name=''):
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

full_name = get_formatted_name('john', 'lee')
print(full_name)

full_name2 = get_formatted_name('john', 'lee', 'hooker')
print(full_name2)