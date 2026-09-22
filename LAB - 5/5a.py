class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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

    def insert_beginning(self, data):
        new = Node(data)
        new.next = self.head
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
        temp.next = new

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    def delete_first(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

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
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


s = SinglyLinkedList()

s.create(10)
s.create(20)
s.create(30)

s.insert_beginning(5)
s.insert_end(40)
s.insert_at_index(25, 3)

s.display()

s.delete_by_value(25)
s.delete_first()
s.delete_last()

s.count()
s.display()