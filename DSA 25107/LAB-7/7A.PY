class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.rear = -1
        self.front = -1
    def enqueue(self,x):
        if self.rear == self.size - 1:
            print("overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear +=1
            self.queue[self.rear] = x
            print("inserted in the queue")
    def dequeue(self):
       if self.front == -1 or self.front>self.rear:
           print("queue underflow")
       else:
           temp = self.queue[self.rear]
           self.queue[self.rear] = None
           self.rear = self.rear + 1
           print(temp,"is deleted")
           if self.front > self.rear:
               self.front = -1
               self.rear = -1

    def peek(self):
       if self.front == -1:
           print("no elements in queue")
       else:
           temp = self.queue[self.rear]
           print(temp, "is the peek")
    def display(self):
       if self.front == -1:
           print("no elements in the queue")
       else:
           while self.front <= self.rear:
               temp = self.queue[self.front]
               print(temp)
               self.front = self.front+1
size = int(input("enter the size of the queue"))
q = Queue(size)
print("queue using arrays")
while True:
    print("1.enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.display")
    print("5.exit")
    selection = int(input("select the index to perform the operation : "))
    if selection == 1:
        x = int(input("enter the element to enqueue"))
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


