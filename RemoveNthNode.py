# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        begin = head
        length = 0
        while head:
            head = head.next 
            length += 1
        head = begin
        want = length - n + 1
        count = 0
        pre = None
        while head:
            count += 1
            if count == want:
                break
            pre = head
            head = head.next
        if pre:
            pre.next = head.next
            return begin
        else:
            return head.next
        