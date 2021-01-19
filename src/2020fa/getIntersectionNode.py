# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # find the length of each linkedList
        m= 0
        n= 0
        A = headA
        B = headB
        while A:
            A = A.next
            m += 1
        while B:
            B = B.next
            n += 1
            
        if m > n: 
            k = m -  n
            return self.FindNode(headB, headA, k)
        else:
            k = n - m 
            return self.FindNode(headA, headB, k)
            
    def FindNode(self, headA, headB, k):
        # assume headA is the shorter linkedList
        count = 0
        while headB:
            if headA == headB:
                return headB
            headB = headB.next
            if count >= k:
                headA = headA.next
            count += 1
        return None