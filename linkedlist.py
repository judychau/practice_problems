#Node is a basic unit of a linked list
#Node class holds two pieces of info: data and pointer to next node 
#self is just a place holder for when the object get instantiated 
class Node(object):
	def __init__ (self, data):
		self.data = data
		self.next = None 

	def __repr__(self):
		return "Node(%s)" % str(self.data)

#how to instantiate a new node
new_node = Node(5)

#A Linked List is just a bunch of nodes linked together. 
#So it starts empty. The only piece of information a 
#Linked List has to have is where it starts, the head.
class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def print_list(self):
		node = self.head

		while node != None:
			print node.data
			node = node.next

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.next
		print count


	def search(self, data):
		current = self.head

		while current != None:
			if current.data == data:
				print True
			current = current.next
		print False


	def add_node(self, data):
		new_node = Node(data)
		#if there is no head, the new node is the head
		if self.head == None:
			self.head = new_node
		#if there is a tail, add the new node to the node after the tail (next)
		if self.tail != None:
			self.tail.next = new_node
		#if there is no tail, the new node is the tail
		self.tail = new_node


	def delete(self, data):
		current = self.head
		prev = None
		found = False

		#search for the node. current will = data once found
		while current and found is False:
			if current.data == data:
				found = True
			else:
				prev = current
				current = current.next
		#empty list
		if current is None: 
			raise ValueError("Data not in list")
		 #if data is found at the head, rebind the head to current.next (bc current=the data we want to remove)
		if prev is None:
			self.head = current.next
		else:
			#prev.next = current so bind it to current.next
			prev.next = current.next
			#set the current node to none to detach it from the list
			current = None

if __name__ == '__main__': 
	linkl= LinkedList()
	linkl.add_node(5)
	linkl.add_node(6)
	linkl.add_node(8)
	linkl.add_node(2)
	linkl.size()
	linkl.search(3)
	linkl.delete(6)
	linkl.print_list()
	linkl.size()















