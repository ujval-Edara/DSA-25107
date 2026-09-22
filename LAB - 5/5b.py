class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new
            new.prev = temp

    def insert_beginning(self, data):
        new = Node(data)

        new.next = self.head

        if self.head:
            self.head.prev = new

        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_beginning(data)
            return

        new = Node(data)
        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new.next = temp.next
        new.prev = temp

        if temp.next:
            temp.next.prev = new

        temp.next = new

    def delete_by_value(self, value):
        temp = self.head

        while temp:
            if temp.data == value:

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                return

            temp = temp.next

        print("Value not found")

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None

    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


d = DoublyLinkedList()

d.create(10)
d.create(20)
d.create(30)

d.insert_beginning(5)
d.insert_end(40)
d.insert_at_index(25, 3)

d.display()

d.delete_by_value(25)
d.delete_first()
d.delete_last()

d.count()
d.display()