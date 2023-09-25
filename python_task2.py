def password_validator(password):
	requirements=False
	special_chars ='[@_!#$%^&*()<>?/\|}{~:]'
	count_upper_chars=0
	count_lower_chars=0
	count_numerics=0
 
	count_special_chars=0

	for each_letter in password:
		if each_letter.isupper()==True:
			count_upper_chars+=1
		if each_letter.islower()==True:
			count_lower_chars+=1
		if each_letter.isnumeric()==True:
			count_numerics+=1
		if each_letter in special_chars:
			count_special_chars+=1

	if count_upper_chars>=2 and count_lower_chars>=2 and count_numerics>=1 and count_special_chars>=3 and len(password)>=10:
		requirements=True
	else:
		requirements=False
	


	print(count_upper_chars)
	print(count_lower_chars)
	print(count_numerics)
	print(count_special_chars)
	print(len(password))
	print(requirements)


#password = input("Enter Password: ")
password = 'okThisIsGoing*^)ToWork1'
password_validator(password)
#response = password_validator(password)
#print(response)