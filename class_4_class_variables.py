class employee:

	raise_amount=1.04 #class variable

	def __init__(self, first, last, pay):
		self.first=first
		self.last=last
		self.pay=pay

	def fullname(self):
		return f"{first} {last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		#self.pay = int(self.pay * employee.raise_amount)

emp_1 = employee('Owais', 'Tahir', 20000)
emp_2 = employee('Test', 'User', 42000)

# print(emp_1.raise_amount)
# print(employee.raise_amount)
# print()
# emp_1.apply_raise()
# emp_2.apply_raise()

# print(emp_1.pay)
# print(emp_2.pay)

# print(employee.__dict__) #we can see that apply_raise is present in the class

#update the raise amount for all the instances
# employee.raise_amount=1.05
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#update the raise amount for only a single instance
emp_1.raise_amount=1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)