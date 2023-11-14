# Python Script to Implement two stacks in a list
import math


class twoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = math.floor(n/2) + 1
        self.top2 = math.floor(n/2)

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = x
            print(f"Element pushed to first stack = ", x)
        else:
            print("Stack Overflow by element : ", x)

    # Method to push an element x to stack2
    def push2(self, x):

        # There is at least one empty space for new element
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
            print(f"Element pushed to second stack = ", x)
        else:
            print("Stack Overflow by element : ", x)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 <= self.size/2:
            x = self.arr[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    # Method to pop an element from second stack
    def pop2(self):
        if self.top2 >= math.floor(self.size/2) + 1:
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


ts = twoStacks(10)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)
ts.push1(1)
ts.push1(2)

print(f"Popped element from first stack is : ", ts.pop1())
ts.push2(40)
print(f"Popped element from second stack is : ", ts.pop2())
