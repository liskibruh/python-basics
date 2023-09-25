class employee:

	raise_amount=1.04 #class variable
	num_of_emps=0


	def __init__(self, first, last, pay):
		self.first=first
		self.last=last
		self.pay=pay
		employee.num_of_emps+=1

	def fullname(self):
		return f"{first} {last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		#self.pay = int(self.pay * employee.raise_amount)


print(employee.num_of_emps)

emp_1 = employee('Owais', 'Tahir', 20000)
emp_2 = employee('Test', 'User', 42000)

print(employee.num_of_emps)