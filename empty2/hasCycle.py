# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Floyd's Tortoise and Hare
        tur = head
        rabbit = head 
        while rabbit or tur:
            tur = tur.next
            rabbit = rabbit.next
            if rabbit == None:
                return False
            else:
                rabbit = rabbit.next
                if rabbit == None:
                    return False
            if tur == rabbit:
                return True
            
            
            