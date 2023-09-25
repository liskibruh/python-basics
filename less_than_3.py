given_number = 1000
count=0

while True:
	if given_number%3==0:
		given_number = given_number/3
		count = count+1
	elif given_number%3!=0:
		given_number=given_number-1
	if given_number<=10:
		break
print(count)