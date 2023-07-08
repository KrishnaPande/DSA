from typing import Optional


class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        curr = head
        # Most optimal solution O(n) and O(1)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    # Move Last Element to Front of a Linked List
    def moveToFront(self, head: Optional['Node']) -> Optional['Node']:
        # code here
        temp = head

        if temp.next == None:
            return temp

        while temp.next.next:
            temp = temp.next

        da = temp.next
        temp.next = None

        da.next = head

        head = da

        return head