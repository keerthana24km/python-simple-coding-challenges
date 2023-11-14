#1
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)
       
def printPreorder(root):
    if root:
        print(root.val, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
       
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" ")


root = Node(10)
root.left = Node(2)
root.right = Node(1)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder traversal of binary tree is")
printInorder(root)
print("\nPreorder traversal of binary tree is")
printPreorder(root)
print("\nPostorder traversal of binary tree is")
printPostorder(root)


#2
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=' ')
        inorder(root.right)


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def deleteNode(root, k):
    if root is None:
        return root


    if root.key > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.key < k:
        root.right = deleteNode(root.right, k)
        return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)


print("\nOriginal BST: ", end='')
inorder(root)


print("\n\nDelete a Leaf Node: 20")
root = deleteNode(root, 20)
print("Modified BST tree after deleting node:")
inorder(root)


#3
from collections import defaultdict
class Graph:


    def __init__(self):


        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.visited=[]


    def BFS(self, s):
        queue = []
        queue.append(s)
        self.visited.append(s)


        while queue:
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(s)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)


print ("\nFollowing is Breath First Traversal (starting from vertex 2)")
g.BFS(2)


#4
class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)


def totalNodes(node):
    if(node == None):
        return 0
   
    l = totalNodes(node.left)
    r = totalNodes(node.right)


    return 1 + l + r


def preorder(node):
    if node is not None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("\nLeaf count of the tree is %d" %(getLeafCount(root)))
print ("\nNumber of nodes in tree is %d" %(totalNodes(root)))
print("\nPreorder traversal of nodes of a tree is")
preorder(root)


#5
class Employee:
    def __init__(self, key, age):
        self.key = key
        self.age = age
        self.next = None
       
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


    def _hash(self, key):
        return hash(key) % self.capacity


    def insert(self, key, age):
        index = self._hash(key)


        if self.table[index] is None:
            self.table[index] = Employee(key, age)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = age
                    return
                current = current.next
            new_node = Employee(key, age)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
           
    def search(self, key):
        index = self._hash(key)


        current = self.table[index]
        while current:
            if current.key == key:
                return current.age
            current = current.next


        raise KeyError(key)
   
    def __str__(self):
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.age))
                current = current.next
        return str(elements)


ht = HashTable(5)


ht.insert("Employee1", 25)
ht.insert("Employee2", 29)
ht.insert("Employee3", 51)
print()
print("Age of the employee is",ht.search("Employee3"))


#6
from collections import defaultdict


class Graph:


    def __init__(self):


        self.graph = defaultdict(list)


    def addEdge(self,u,v):
        self.graph[u].append(v)


    def DFSUtil(self, v, visited):
        visited[v]= True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                print("Connected component {} -> {}".format(v,i))
                self.DFSUtil(i, visited)


    def DFS(self):
        V = len(self.graph)
        visited =[False]*(V)
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print("\nFollowing is Depth First Traversal")
g.DFS()


#7
class Graph:
    adj = []
    def __init__(self, v, e):
        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)]
                        for j in range(v)]


    def addEdge(self, start, e):
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1


    def BFS(self, start):
        visited = [False] * self.v
        q = [start]
        visited[start] = True
        while q:
            vis = q[0]
            print(vis, end = ' ')
            q.pop(0)
            for i in range(self.v):
                if (Graph.adj[vis][i] == 1 and
                    (not visited[i])):
                    q.append(i)
                   
                    visited[i] = True


v, e = 5, 4
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(1, 3)
print("\nFollowing is the BFS traversal")
G.BFS(0)
print()


#8
d = 256
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
   
    for i in range(M-1):
        h = (h * d)% q


    for i in range(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q


    for i in range(N-M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break


            j+= 1
            if j == M:
                print("Pattern found at index " + str(i))


        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q


            if t < 0:
                t = t + q


txt = "IT IS ITENARY ITERATIVES"
pat = "IT"
q = 101
search(pat, txt, q)


#9
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


    def __lt__(self, nxt):
        return self.freq < nxt.freq


def printNodes(node, val=''):
    newVal = val + str(node.huff)  
    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newVal}")


chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))


while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)


print("\nHuffman Coding")
printNodes(nodes[0])