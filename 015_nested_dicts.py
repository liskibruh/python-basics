users={
		'aeinstein':{
					'first':'albert', 
					'last':'einstein', 
					'location':'princeton',
					}, 
		'mcurie':{
					'first':'marie',
					'last':'curie',
					'location':'paris',},
		}


for username, user_info in users.items():
	print(f"Username: {username}")
	print(f"First Name: {user_info['first']}")
	print(f"Last Name:{user_info['last']}" )
	print()