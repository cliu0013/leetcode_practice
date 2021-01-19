# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Runtime O(max(lengthl1, lengthl2))
        # space
        length1 = 0
        length2 = 0
        a = l1
        b = l2
        while a:
            a = a.next
            length1 += 1
        while b:
            b = b.next
            length2 += 1
        k = max(length1, length2) - min(length1, length2)
        if length1 > length2:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1
        count = 0
        node = ListNode(0, None)
        begin = node
        while count < k:
            node.next = shorter 
            shorter = node
            node = ListNode(0, None)
            count+= 1
        # print(longer)
        # print(shorter)
        curnode, cin = self.addTwo(shorter, longer)
        if cin:
            res = ListNode(1, curnode)
            return res
        else:
            return curnode
        
    def addTwo(self, node1, node2):
        curnode = ListNode(0, None)
        if node1.next == None and node2.next == None:
            res, cin = (node1.val+node2.val) % 10, int((node1.val+node2.val) / 10)
            curnode.val = res
            return curnode, cin
        else:
            nextNode, cin = self.addTwo(node1.next, node2.next)
            res = ((node1.val+node2.val) +  cin)% 10 
            cin = int(((node1.val+node2.val) +  cin)/10)
            curnode.next = nextNode
            curnode.val = res
            return curnode, cin
            
            
            