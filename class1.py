class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle

class child_vehicle(vehicle):

    def result_child_vehicle(self,seating_capacity):
        return self.name_of_vehicle, seating_capacity

child_obj = child_vehicle('Toyota', 120, 70)

print(child_obj.result_child_vehicle(8))