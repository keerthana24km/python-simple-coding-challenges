# Python program for the above approach
# link list node
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
llist1 = LinkedList()
llist2 = LinkedList()

print("Enter elements into first list in sorted order")
for i in range(5):
	i = int(input())
	if(i!=999):
		llist1.push(i)
	else:
		break
	
print("Enter elements into second list in sorted order")
for i in range(5):
	i = int(input())
	if(i!=999):
		llist2.push(i)
	else:
		break

v = []
temp = llist1.head
while(temp is not None):
	v.append(temp.key)
	temp = temp.next


temp = llist2.head
while(temp is not None):
	v.append(temp.key)
	temp = temp.next

v.sort()
result = Node(-1)
temp = result
for i in range(len(v)):
	result.next = Node(v[i])
	result = result.next

temp = temp.next
print("Resultant Merge Linked List is : ")
while(temp is not None):
	print(temp.key, end=" ")
	temp = temp.next
