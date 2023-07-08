class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None
        self.n = 0

    def insert_head(self, value):

        # Create a Node
        new_node = Node(value)

        # Create Connection
        new_node.next = self.head

        # Re-assigning head
        self.head = new_node

        # Increment n
        self.n = self.n + 1

    # My Code
    def max(self):

        pos = 0
        curr = self.head

        while curr != None:
            if curr.data > pos:
                pos = curr.data
        print(pos)

        while curr != None:
            if curr.data != pos:
                print(curr.data)
        print(pos)

    # Code form campusX
    def replace_max(self, value):

        temp = self.head

        max = temp

        while temp != None:
            if temp.data > max.data:
                max = temp
            temp = temp.next

        max.data = value

    def traverse(self):

        curr = self.head

        while curr != None:
            print(curr.data)
            curr = curr.next
        print("----->->->")
    def sum_odd_nodes(self):

        temp = self.head
        coun = 0

        su = 0

        while temp != None:
            if coun %2 != 0:
                su += temp.data
            coun += 1
            temp = temp.next

        print(su)


l = LL()

l.insert_head(5)
l.insert_head(7)
l.insert_head(55)
l.insert_head(9)
l.insert_head(2)
l.sum_odd_nodes()
l.traverse()

print(l)

