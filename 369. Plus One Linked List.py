'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self, head):
        prev = None
        temp = head
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    def addOne(self,head):
        #Returns new head of linked List.
        newhead = self.reverse(head)
        carry = 1
        temp = newhead
        while carry and temp:
            sum = temp.data + carry if temp else carry
            carry = sum//10
            sum = sum%10
            temp.data = sum
            temp = temp.next
        newhead = self.reverse(newhead)
        if carry:
            newnode = Node(carry)
            newnode.next = newhead
            newhead = newnode
        return newhead