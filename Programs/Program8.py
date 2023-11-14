# Creating a node class
class Node:
    def __init__(self, name, rollno, mathmarks, scimarks):
        self.name = name
        self.rollno = rollno
        self.mathmarks = mathmarks
        self.scimarks = scimarks
        self.next = None  # Initally this node will not be linked with any other node
        self.prev = None  # It will not be linked in either direction


# Creating a doubly linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initally there are no elements in the list
        self.tail = None

    # Adding an element before the first element
    def insert(self, new_name, new_rollno, new_marks1, new_marks2):
        # creating a new node with the desired value
        new_node = Node(new_name, new_rollno, new_marks1, new_marks2)
        # newly created node's next pointer will refer to the old head
        new_node.next = self.head

        if self.head != None:  # Checks whether list is empty or not
            # old head's previous pointer will refer to newly created node
            self.head.prev = new_node
            self.head = new_node  # new node becomes the new head
            new_node.prev = None

        else:  # If the list is empty, make new node both head and tail
            self.head = new_node
            self.tail = new_node
            new_node.prev = None  # There's only one element so both pointers refer to null

    def print_details(self):
        if self.head is None:
            print("The list is empty")
        else:
            print("Student Details\n")
            n = self.head
            while n is not None:
                print("Student name: ", n.name)
                print("Student RollNo: ", n.rollno)
                print("Student Math marks: ", n.mathmarks)
                print("Student Science marks: ", n.scimarks)
                n = n.next
            print("\n")

    def studmorethan90(self):
        n = self.head
        while n is not None:
            if (n.mathmarks >= 90 and n.scimarks >= 90):
                print(f"Student with marks more than 90 in Math and Science is ", n.name)
            n = n.next


stud = DoublyLinkedList()
stud.insert("Keerthana", 1234, 92, 99)
stud.insert("Bharath", 1245, 94, 91)
stud.insert("Nithya", 1346, 88, 90)
stud.insert("Nithin", 1256, 82, 85)
stud.print_details()
stud.studmorethan90()
