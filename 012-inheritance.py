"""
you can add to or redefine the capabilities of 
existing classes via inheritance. Suppose you 
wanted to add a method to swap the top two items 
on the stack:
"""

class Stack:
	def __init__(self):
		self._items=[]

	def push(self, item):
		self._items.append(item)

	def pop(self):
		return self._items.pop()

	def display_stack(self):
		print(self._items)


class SwapStack(Stack):
	def swap(self):
		a = self.pop()
		b = self.pop()
		self.push(a)
		self.push(b)


"""
Inheritance can also be used to change the 
behavior ofan existing method. Suppose you 
want to restrict the stack to only hold 
numeric data. Write a class like this:
"""

class NumericStack(Stack):
	def push(self, item):
		if not isinstance(item, (int,float)):
			raise TypeError("Expected an int or float")

		super().push(item)

"""
the push() method has been redefined to add extra 
checking. The super() operation is a way to 
invoke the prior definition of push()
"""

n = NumericStack()
n.push(41)
#n.push('Dave') this will throw typeError
n.display_stack()