#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        count0, count1, count2 = 0,0,0
        temp = head
        while temp:
            if temp.data == 0:
                count0 += 1
            elif temp.data == 1:
                count1 += 1
            else:
                count2 += 1
            temp = temp.next
        temp = head
        while temp:
            if count0 > 0:
                temp.data = 0
                count0 -= 1
            elif count1 > 0:
                temp.data = 1
                count1 -= 1
            else:
                temp.data = 2
                count2 -= 1
            temp = temp.next
        return head
    