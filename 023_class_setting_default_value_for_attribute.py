class Car():
	def __init__(self, make, model, year):
		self.make=make
		self.model=model
		self.year=year

		#set a parameter with default value
		self.odometer_reading=0

	def get_descriptive_name(self):
		print(f"My new car is {self.make.title()} {self.model.title()}")

	def read_odometer(self):
		print(f"The car has {self.odometer_reading} miles on it")


my_new_car=Car('audi', 'a4', 2019)
my_new_car.get_descriptive_name()
my_new_car.read_odometer()