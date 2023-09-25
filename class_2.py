class employee:
	def __init__(self, first, last): #constructor
		self.first=first #same as emp_1/emp_2.first=first
		self.last = last #same as emp_1/emp_2.last=last


emp_1 = employee("Owais","Tahir")
emp_2 = employee("Test", "User")

print(emp_1.first)
print(emp_2.first)