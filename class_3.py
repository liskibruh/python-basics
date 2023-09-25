class employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	def fullname(self):
		return f"{self.first} {self.last}"



emp_1 = employee("Owais", "Tahir")

full_name=emp_1.fullname()
#employee.fullname(emp_1) #same as emp_1.fullname()

print(full_name)