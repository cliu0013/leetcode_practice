# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head

        res = odd = head
        even = head.next

        while head:
            temp = head.next
            if head.next:
                head.next = head.next.next
            head = temp
        
        while odd.next:
            odd = odd.next
        odd.next = even

        return res
                        
#         if not head:
#             return head
        
#         odd = ListNode(head.val, None)
#         begin_odd = odd
#         if not head.next:
#             return odd
#         even = ListNode(head.next.val, None)
#         begin_even = even

#         count = 3
#         head = head.next.next
#         while head:
#             if count % 2 == 0:
#                 even.next = ListNode(head.val, None)
#                 even = even.next
#             else:
#                 odd.next = ListNode(head.val, None)
#                 odd = odd.next
#             head = head.next
#             count += 1
#         odd.next = begin_even
#         return begin_odd