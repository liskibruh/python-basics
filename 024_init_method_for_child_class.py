class Car():
	def __init__(self, make, model, year):
		self.make=make
		self.model=model
		self.year=year

		#set a parameter with default value
		self.odometer_reading=0

	def get_descriptive_name(self):
		print(f"{self.year} {self.make.title()} {self.model.title()}")

	def read_odometer(self):
		print(f"The car has {self.odometer_reading} miles on it")


class ElectricCar(Car):
	"""
	represents aspects of a car, specific to electric vehicles
	"""
	def __init__(self, make, model, year):
		#initialize attributes of the parent class
		super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())