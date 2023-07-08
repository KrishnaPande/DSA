class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):
        self.head = None
        self.n = 0

    def insert_head(self, value):

        temp = Node(value)

        temp.next = self.head

        self.head = temp


    def traverse(self):

        curr = self.head

        while curr:
            print(curr.data, end='->')
            curr = curr.next

    def change_sen(self):

        temp = self.head

        while temp:
            if temp.data == "/" or temp.data == "*":
                temp.data = " "
                if temp.next.data == "/" or temp.next.data == "*":
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next

            temp = temp.next
#git

s = LL()

s.insert_head("k")
s.insert_head("*")
s.insert_head("m")
s.insert_head("/")
s.insert_head("s")
s.insert_head("/")
s.insert_head("*")
s.insert_head("k")
s.insert_head("S")
s.insert_head("S")
s.insert_head("p")
s.insert_head("a")
s.insert_head("n")
s.insert_head("d")
s.insert_head("e")
s.insert_head(":")
s.traverse()
s.change_sen()
s.traverse()

