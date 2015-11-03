# A stack is an unordered collection of items where 
# items are added and removed from the end (the top). 
# Last in first out (LIFO)
class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		if self.items == []:
			print True
		else:
			print False

	def push(self, item):
		self.items.append(item)

	def pop(self):
		print self.items.pop()

	def peek(self):
		print self.items[-1]

	def size(self):
		print len(self.items)

	def print_stack(self):
		print self.items

# A queue is an unordered collection of items where 
# items are added at the rear (end) and items removed are at the front (top)
# First in first out (FIFO) (ex: line)
class Queue():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		if self.items == []:
			print True
		else:
			print False

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		print len(self.items)

	def print_queue(self):
		print self.items


if __name__ == '__main__': 
	# s= Stack()
	# s.isEmpty()
	# s.push(3)
	# s.push(4)
	# s.push(5)
	# s.print_stack()
	# s.peek()
	# s.pop()
	# s.size()
	q= Queue()
	q.isEmpty()
	q.enqueue(2)
	q.enqueue(3)
	q.enqueue(4)
	q.enqueue(5)
	q.print_queue()
	q.dequeue()
	q.print_queue()
	q.size()
