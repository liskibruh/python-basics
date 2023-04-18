class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name=name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"Restaurant name is {self.name}")
		print(f"Cuising type is {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.name} is now open!")

class User():
	def __init__(self, first_name, last_name, age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age

	def describe_user(self):
		print(f"User's name is {self.first_name} {self.last_name}")
		print(f"User's age is {self.age}")

	def greet_user(self):
		print(f"Greetings {self.first_name} {self.last_name}!")


curry_kingdom = Restaurant("Curry Kingdom", "Mexican-American")
silver_spoons = Restaurant("Silver Spoons", "Chinese American")
am_dining_room = Restaurant("Americana Dining Room", "Filipino-American")

user_ali = User("Muhammad", "Ali",22 )
user_khan = User("Akram", "Khan",45)

curry_kingdom.describe_restaurant()
silver_spoons.describe_restaurant()
am_dining_room.describe_restaurant()

user_khan.describe_user()
user_khan.greet_user()

user_ali.describe_user()
user_ali.greet_user()