class Restaurant:
	def __init__(self, name, cuisine_type):
		self.name=name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print(f"Restaurant name is {self.name}")
		print(f"Cuising type is {self.cuisine_type}")

	def open_restaurant(self):
		print(f"{self.name} is now open!")

class IceCreamStand(Restaurant):
	def __init__ (self):
		self.flavors=['Chocolate','Vanilla','Strawberry']

	def describe_flavors(self):
		print(f"This stand serves the following flavors: {self.flavors}")

class User:
	def __init__(self, first_name, last_name, age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age

	def describe_user(self):
		print(f"User's name is {self.first_name} {self.last_name}")
		print(f"User's age is {self.age}")

	def greet_user(self):
		print(f"Greetings {self.first_name} {self.last_name}!")


class Previleges:
	def __init__ (self):
		self.previleges = ['can add post', 'can delete post', 'can ban user']

	def show_previleges(self):
		print(f"This admin has the following previleges: {self.previleges}")


class Admin(User):
	def __init__(self):
		self.previleges=Previleges()


ice_cream_stand = IceCreamStand()
ice_cream_stand.describe_flavors()

admin_1 = Admin()
admin_1.previleges.show_previleges()
