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
            sum = temp.data + carry 
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
#Recursive solution added
class Solution:
    def add_one_recursive(self,node):
            if not node:
                return 1  # Carry for an empty node is 1
            
            carry = self.add_one_recursive(node.next)
            node.data += carry
            if node.data< 10:
                return 0
            node.data = 0
            return 1
        
        
    def addOne(self,head):
        #Returns new head of linked List.
        temp = head
        carry = self.add_one_recursive(head)
        if carry:
            newhead = Node(1)
            newhead.next = head
            return newhead
        return head
        