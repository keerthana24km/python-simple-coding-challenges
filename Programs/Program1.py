# Class definition for Node
class Node:
	# Initialize the node with a key
	def __init__(self, id, name, designation, salary):
		self.id = id
		self.name = name
		self.designation = designation
		self.salary = salary
		self.next = None

# Class definition for Linked List
class LinkedList:
	# Initialize the linked list with a head node
	def __init__(self):
		self.head = None

	# Add a new node with key "new_key" at the beginning of the linked list
	def push(self, new_id, new_name, new_d, new_salary):
		new_node = Node(new_id, new_name, new_d, new_salary)
		new_node.next = self.head
		self.head = new_node

# Create a linked list object
llist = LinkedList()

# Add new nodes to the linked list
llist.push(101, "Keerthana", "Software Engineer", 50000)
llist.push(102, "Disha", "Senior Software Dev", 79000)
llist.push(103, "Anjali", "SME", 66000)
llist.push(104, "John", "CEO", 120000)
llist.push(105, "Elisa", "PM", 85000)
# Key to search for in the linked list
x = int(input("Enter the id to be searched "))

# Create a temp variable to traverse the linked list
temp = llist.head
c=0
sumsal=0
while(temp):
	sumsal += temp.salary
	temp = temp.next
	c+=1
print(f"Average of all employee salaries = ",(sumsal/c))

# List to store the keys in the linked list
v = []

# Traverse the linked list and store the keys in the list "v"
temp = llist.head
while(temp):
	v.append(temp.id)
	temp = temp.next

# Check if "x" is in the list "v"
if x in v:
	val = llist.head
	while(val.next != None):
		if val.id == x:
			print(val.id)
			print(val.name)
			print(val.designation)
			print(val.salary)
			break
		else:
			val = val.next
else:
	print("ID not found..")
