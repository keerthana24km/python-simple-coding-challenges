# A single node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None, next=None, num=0):
        self.data = data
        self.next = next
        self.num = num

# A Linked List class with a single head node


class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
            self.num += 1
        else:
            self.head = newNode
            self.num = 1

    def delete(self):
        if (self.head is None):
            print("List is Empty\n")
        else:
            current = self.head
            self.head = current.next
            current.next = current.next.next
            self.num -= 1

    # print method for the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next
        print(f"Number of elements = ", self.num)


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
LL.delete()
LL.delete()
LL.printLL()
