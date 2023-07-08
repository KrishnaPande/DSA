class Node:

    def __init__(self, data):

        self.data = data
        self.next = None

class LL:

    def __init__(self):

        self.head = None
        self.n = 0

    def traverse(self):

        curr = self.head

        while curr != None:
            curr.data
        curr = curr.next

    def reverse(self):

        temp = self.head
        prev_node = None
        curr_node = self.head

        while temp != None:
            next_node = curr_node.next
            curr_node.next = prev_node
