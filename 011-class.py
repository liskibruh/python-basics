"""
The class statement is used to define new types of objects and for 
object-oriented programming. For example, the following class defines 
a stack with push() and pop() operations:
"""

class Stack:
	def __init__ (self):
		self._items = [] #items is a private variable, not used outside the Stack class

	def push(self, item):
		self._items.append(item)

	def pop(self):
		return self._items.pop()

	def display_stack(self):
		print(self._items)


s = Stack()
s.push('Dave')
s.push(1)
s.push([2])

y=s.pop() #pop [2] from the stack and assign to y
s.display_stack()
print(y)