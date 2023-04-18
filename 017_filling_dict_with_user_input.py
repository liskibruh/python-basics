responses = {}

#set a flag to indicate that polling is active
polling_active = True

while polling_active:
	name = input('What is your name?')
	response = input('Which mountain would you like to climb someday?')

	responses[name]=responses

	repeat = "Would you like to let another person respond? (y/n)"
	if repeat=='n':
		polling_active=False

	#polling is complete, show the results
	for name, response in responses.items():
		print(f"Name: {name}")
		print(f"Response: {response}")
		print()