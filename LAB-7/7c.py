class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = x

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        x = self.queue[self.front]

        print("Deleted element:", x)

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[self.front])

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return

        print("Queue:", end=" ")

        i = self.front

        while True:
            print(self.queue[i], end=" ")

            if i == self.rear:
                break

            i = (i + 1) % self.size

        print()


size = int(input("enter the size of the queue: "))
q = Queue(size)

print("circular queue")

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