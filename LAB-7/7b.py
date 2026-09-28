class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new = Node(x)

        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        x = self.front.data
        self.front = self.front.next

        print("Deleted element:", x)

        if self.front is None:
            self.rear = None

    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front element:", self.front.data)

    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front

        print("Queue:", end=" ")

        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


q = Queue()

print("queue using linked list")

while True:
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.display")
    print("5.exit")

    selection = int(input("select the index to perform the operation : "))

    if selection == 1:
        x = int(input("enter the element to enqueue: "))
        q.enqueue(x)

    elif selection == 2:
        q.dequeue()

    elif selection == 3:
        q.peek()

    elif selection == 4:
        q.display()

    elif selection == 5:
        break

    else:
        print("invalid selection")