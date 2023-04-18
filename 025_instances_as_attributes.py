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


class Battery:
	def __init__(self, battery_size=75):
		self.battery_size=battery_size

	def describe_battery(self):
		print(f"This cas has {self.battery_size}-kWh battery")

	def get_range(self):
		if self.battery_size == 75:
			range=260
		elif self.battery_size == 100:
			range=315

		print(f"This car can go about {range} miles on full charge")

	def upgrade_battery(self):
		if self.battery_size!=100:
			self.battery_size=100

class ElectricCar(Car):
	"""
	represents aspects of a car, specific to electric vehicles
	"""
	def __init__(self, make, model, year):
		#initialize attributes of the parent class
		super().__init__(make, model, year)
		#instance as attribute
		self.battery=Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
#my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()