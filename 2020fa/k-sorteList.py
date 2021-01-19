# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        n = len(lists)
        
        if n == 0:
            return None
        
        res = lists[0]
        
        if n == 1:
            return res
        
        if n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        
        else:
            half = int(n/2)
            left = self.mergeKLists(lists[0:half])
            right = self.mergeKLists(lists[half:])
            return self.mergeTwoLists(left, right)
    
    
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(0)
        prev = prehead
            
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
            
        prev.next = l1 if l1 is not None else l2

        return prehead.next