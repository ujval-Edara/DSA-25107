class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            print(temp.data, "popped from stack")
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Top element:", self.top.data)

    def display(self):
        temp = self.top

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()
s.pop()
s.display()