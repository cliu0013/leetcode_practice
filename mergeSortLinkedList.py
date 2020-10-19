# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        length = 0 
        h = head
        while h:
            h = h.next
            length += 1
        if length % 2  == 0:
            half = int(length/2)
        else:
            half = int(length/2) + 1
        if length == 1:
            return head
        
        
        left = head
        right = head
        count  = 0
        while count < half:
            if count == half- 1:
                temp = right
                right = right.next
                temp.next = None
            else:
                right = right.next
            count += 1
            
            
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def merge(self, left, right):
        head = left
        res = None
        pre = None
        
        if not left:
            return right
        if not right:
            return left
        
        if left.val <= right.val:
            res = left
        else:
            res = right
    
        
        while head and right:
            if right.val < head.val:
                temp = right
                if pre:
                    pre.next = right
                pre = right
                right = right.next
                temp.next = head
            else:
                temp = head
                if pre:
                    pre.next = head
                pre = head
                head = head.next
                temp.next = right
        return res
                
            