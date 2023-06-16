class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.items = []
		pass
	
	def push(self, item):
		# Push an item to the stack
		return self.items.insert(0,item)
		pass

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		if self.items==[]:
			return "Error"
		else:
			return self.items[0]
		pass

	def pop(self):
		# Pop an item from the stack if non-empty
		if self.is_empty():
			return "Error"
		else:
			return self.items.pop(0)
		pass

	def is_empty(self):
		# Return True if stack is empty, False otherwise
		return self.items==[]
		pass

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"

		a=""
		for i in self.items:
			a+= str(i)
			a+= " "
		return a
		pass

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.items)
		pass