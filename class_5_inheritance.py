class employee:

	raise_amount=1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@email.com'

	def full_name(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay*self.raise_amount)


class developer(employee):
	pass


dev_1 = developer('Owais', 'Tahir', 50000)
dev_2 = developer('Test', 'User', 60000)
#python first looks for init method in the developer class
#when it does not find it there, python walks up the inheritence chain
#path and look for it in the base classes until it finds it
#the chain is called the method resolution order

print(dev_1.email)
print(dev_2.email)

print(help(developer))