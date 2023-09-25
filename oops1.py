class vehicle:
	def __init__(self, vehicle_name, max_speed, vehicle_average):
		self.vehicle_name= vehicle_name
		self.max_speed = max_speed
		self.vehicle_average = vehicle_average

class car(vehicle):
	def seating_capacity(self, seating_capacity):
		return self.vehicle_name,seating_capacity


car_obj = car('Toyota', 140, 100)

print(car_obj.seating_capacity(6))