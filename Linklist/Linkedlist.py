"""
A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
Lenght of Linkedlist is Number of Nodes
"""

class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):

        # Create a Node
        new_node = Node(value)

        # Create Connection
        new_node.next = self.head

        # Re-assigning head
        self.head = new_node

        # Increment n
        self.n = self.n + 1

    def __str__(self):

        current = self.head

        result = ''

        while current != None:
            result = result + str(current.data) + '->'
            current = current.next

        return result[:-2]

    # Inserting a value to tail
    def append(self, value):

        # Create a New_node
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            # Next line will not be executed because of return
            return

        curr = self.head

        while curr.next != None:
            curr = curr.next

        # You are at the tail
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):

        # Create a new_node
        new_node = Node(value)

        # Assign curr variable as head, (We can directly jump on after)
        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        # This logic if for the case when after is not in the LL
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return "Item Not Found"

    def clear(self):

        self.head = None
        self.n = 0

    def del_head(self):

        if self.head == None:
            return "Empty LL"
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):

        curr = self.head

        # When LL is Empty
        if self.head == None:
            return "LL is Empty"

        # When LL has one item and next of curr is None (curr is self.head) for now
        if curr.next == None:
            self.del_head()

        # Logic will not work if 1 item is there in LL
        while curr.next.next != None:
            curr = curr.next

        curr.next = None
        self.n = self.n - 1

    def remove(self, value):

        curr = self.head

        if curr.data == None:
            return "Empty LL"

        if curr.data == value:
            self.del_head()

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            # item not found
            return "Not Found"
        else:
            curr.next = curr.next.next

    def search(self, item):

        curr = self.head
        pos = 0

        while curr.next != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1

        return "Not Found"

    def __getitem__(self, item):

        curr = self.head
        pos = 0

        while curr != None:
            if pos == item:
                return pos
            curr = curr.next
            pos += 1


'''
Note work as after is int type note a node which have data and value
        # Traverse thill we find after
        while curr.data != after:
            curr = curr.next

        # Ones after is found assign new_node next to after next
        new_node.next = after.next

        # After next to new node
        after.next = new_node
'''


s = Linkedlist()

s.insert_head(4)
s.insert_head(7)
s.insert_head(55)
s.insert_head(1)
print(s)
s.append(77)
s.remove(77)
s.search(55)
print(s.search(200))
print(s)
print(s[0])
s[0]
















"""
s.del_head()
print(s)
# How to create Individual Nodes and connect them?
# Created 3 Node a, b, c
a = Node(3)
b = Node(4)
c = Node(5)

# Added Next Manually
a.next = b
b.next = c
print(a.data)
print(b.data)
print(c.data)
print(a.next)
print(b.next)
"""