# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        begin = head
        pre = None
        k = n - m + 1
        count = 0
        while count < m - 1:
            pre = head
            head = head.next
            count += 1
        left = pre
        first = self.reverseLinkedList(head, k)
        if left: 
            left.next = first
            return begin
        else:
            return first
    
    def reverseLinkedList(self, head, k):
        last = head
        count = 0
        pre = nex = None
        while head and count < k:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
            count += 1
        first = pre
        last.next = head
        return first
    