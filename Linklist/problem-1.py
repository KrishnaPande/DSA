# Nth node from end of linked list
def getNthFromLast(head, n):
    # code here
    temp = head

    len = 0
    while temp:
        len += 1
        temp = temp.next

    if len < n:
        return -1

    cou = len - n

    temp = head
    while cou > 0:
        temp = temp.next
        cou -= 1

    return temp.data

# Finding middle element in a linked list
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node

        temp = head
        len = 0

        while temp:
            len += 1
            temp = temp.next
        temp = head
        if len % 2 == 0:
            count = len / 2
            while count > 0:
                temp = temp.next
                count -= 1
        else:
            count = (len + 1) / 2
            while count > 1:
                temp = temp.next
                count -= 1

        return temp.data