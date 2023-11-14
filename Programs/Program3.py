class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
		
# Class definition for Linked List
class LinkedList:
	# Initialize the linked list with a head node
	def __init__(self):
		self.head = None

	# Add a new node with key "new_key" at the beginning of the linked list
	def push(self, new_key):
		new_node = Node(new_key)
		new_node.next = self.head
		self.head = new_node

# Create a linked list object
llist = LinkedList()
c=0

print("Enter elements into the list")
for i in range(10):
	i = int(input())
	if(i!=999):
		llist.push(i)
		c+=1
	else:
		break
	
half = c//2
first_llist = LinkedList()
last_llist = LinkedList()

temp = llist.head
for i in range(c,half,-1):
	last_llist.push(temp.key)
	temp = temp.next

for i in range(half,0,-1):
	first_llist.push(temp.key)
	temp = temp.next
	
print("First half of the list")
temp = first_llist.head
while(temp!=None):
	print(temp.key)
	temp = temp.next
	
print("Second half of the list")
temp = last_llist.head
while(temp!=None):
	print(temp.key)
	temp = temp.next